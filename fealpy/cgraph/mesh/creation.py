from typing import Type
import importlib

from ..nodetype import CNodeType, PortConf, DataType


def get_mesh_class(mesh_type: str) -> Type:
    m = importlib.import_module(f"fealpy.mesh.{mesh_type}_mesh")
    mesh_class_name = mesh_type[0].upper() + mesh_type[1:] + "Mesh"
    return getattr(m, mesh_class_name)


class Box2d(CNodeType):
    r"""Create a mesh in a box-shaped 2D area.

    Inputs:
        mesh_type (str): Type of mesh to granerate.
        domain (tuple[float, float, float, float], optional): Domain.
        nx (int, optional): Segments on x direction.
        ny (int, optional): Segments on y direction.

    Outputs:
        mesh (MeshType): The mesh object created.
    """
    TITLE: str = "二维 Box 网格"
    PATH: str = "网格.构造"
    INPUT_SLOTS = [
        PortConf("mesh_type", DataType.MENU, 0, title="网格类型", default="triangle", items=["triangle", "quadrangle"]),
        PortConf("domain", DataType.NONE, title="区域"),
        PortConf("nx", DataType.INT, title="X 分段数", default=10, min_val=1),
        PortConf("ny", DataType.INT, title="Y 分段数", default=10, min_val=1)
    ]
    OUTPUT_SLOTS = [
        PortConf("mesh", DataType.MESH, title="网格")
    ]

    @staticmethod
    def run(mesh_type, domain, nx, ny):
        MeshClass = get_mesh_class(mesh_type)
        kwds = {"nx": nx, "ny": ny}
        if domain is not None:
            kwds["box"] = domain
        return MeshClass.from_box(**kwds)
    

class DLDMicrofluidicChipMesh2d(CNodeType):
    
    TITLE: str = "二维 DLD 微流芯片网格"
    PATH: str = "网格.构造"
    INPUT_SLOTS = [
        PortConf("init_point", DataType.FLOAT, 0, default=(0.0,0.0), title="初始点"),
        PortConf("chip_height", DataType.FLOAT, 0, default=1.0, title="芯片高度"),
        PortConf("inlet_length", DataType.FLOAT, 0, default=0.1, title="入口宽度"),
        PortConf("outlet_length", DataType.FLOAT, 0, default=0.1, title="出口宽度"),
        PortConf("radius", DataType.FLOAT, 0, default=1 / (3 * 4 * 3), title="微柱半径"),
        PortConf("n_rows", DataType.INT, 0, default=8, title="行数"),
        PortConf("n_cols", DataType.INT, 0, default=4, title="列数"),
        PortConf("tan_angle", DataType.FLOAT, 0, default=1/7, title="偏转角正切值"),
        PortConf("n_stages", DataType.INT, 0, default=3, title="微柱阵列周期数"),
        PortConf("stage_length", DataType.FLOAT, 0, default=1.4, title="单周期长度"),
        PortConf("lc", DataType.FLOAT, 0, default=0.02, title="网格尺寸")
    ]
    OUTPUT_SLOTS = [
        PortConf("mesh", DataType.MESH, title="网格"),
        PortConf("radius", DataType.FLOAT, title="微柱半径"),
        PortConf("centers", DataType.FLOAT, title="微柱圆心坐标"),
        PortConf("inlet_boundary", DataType.TENSOR, title="入口边界"),
        PortConf("outlet_boundary", DataType.TENSOR, title="出口边界"),
        PortConf("wall_boundary", DataType.TENSOR, title="通道壁面边界")
    ]

    @staticmethod
    def run(**options):
        from fealpy.geometry import DLDMicrofluidicChipModeler
        from fealpy.mesher import DLDMicrofluidicChipMesher
        import gmsh

        options = {
            "init_point" : options.get("init_point"),
            "chip_height" : options.get("chip_height"),
            "inlet_length" : options.get("inlet_length"),
            "outlet_length" : options.get("outlet_length"),
            "radius" : options.get("radius"),
            "n_rows" : options.get("n_rows"),
            "n_cols" : options.get("n_cols"),
            "tan_angle" : options.get("tan_angle"),
            "n_stages" : options.get("n_stages"),
            "stage_length" : options.get("stage_length"),
            "lc" : options.get("lc")
        }

        gmsh.initialize()
        modeler = DLDMicrofluidicChipModeler(options)
        modeler.build(gmsh)
        mesher = DLDMicrofluidicChipMesher(options)
        mesher.generate(modeler, gmsh)
        # gmsh.fltk.run()
        gmsh.finalize()

        return (mesher.mesh, mesher.radius, mesher.centers, mesher.inlet_boundary, 
                mesher.outlet_boundary, mesher.wall_boundary)


class SphereSurface(CNodeType):
    r"""Create a mesh on the surface of a unit sphere.

    Inputs:
        mesh_type (str): Type of mesh to granerate.
        refine (int): Number of mesh refine times.

    Outputs:
        mesh (MeshType): The mesh object created.
    """
    TITLE: str = "球面网格"
    PATH: str = "网格.构造"
    DESC: str = "生成单位球面上的网格，输出网格类型与网格加密次数，加密次数越大，网格越密。"
    INPUT_SLOTS = [
        PortConf("mesh_type", DataType.MENU, 0, default="triangle", items=["triangle", "quadrangle"]),
        PortConf("refine", DataType.INT, 0, default=2, min_val=1),
    ]
    OUTPUT_SLOTS = [
        PortConf("mesh", DataType.MESH)
    ]

    @staticmethod
    def run(mesh_type, refine):
        MeshClass = get_mesh_class(mesh_type)
        kwds = {"refine": refine}
        return MeshClass.from_unit_sphere_surface(**kwds)
    
class Sphere(CNodeType):
    r"""Create a mesh of a unit sphere.

    Inputs:
        mesh_type (str): Type of mesh to granerate.
        h (float): The mesh density, the smaller the h, the denser the grid.

    Outputs:
        mesh (MeshType): The mesh object created.
    """
    TITLE: str = "球体网格"
    PATH: str = "网格.构造"
    DESC: str = "生成单位球体的网格，输入网格类型和网格密度h。h一般为大于0小于1的浮点数，h越小，网格越密。"
    INPUT_SLOTS = [
        PortConf("mesh_type", DataType.MENU, 0, default="tetrahedron", items=["tetrahedron"]),
        PortConf("h", DataType.FLOAT, 0, default=0.5, min_val=0.1),
    ]
    OUTPUT_SLOTS = [
        PortConf("mesh", DataType.MESH)
    ]

    @staticmethod
    def run(mesh_type, h):
        MeshClass = get_mesh_class(mesh_type)
        kwds = {"h": h}
        return MeshClass.from_unit_sphere_gmsh(**kwds)