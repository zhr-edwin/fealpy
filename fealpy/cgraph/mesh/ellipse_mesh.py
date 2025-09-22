from fealpy.cgraph.nodetype import CNodeType, PortConf, DataType

class Ellipse2d(CNodeType):
    r"""Generate a mesh for an ellipse.

    Inputs:
        a (float): semi-major axis.
        b (float): semi-minor axis.
        center (list): center of the ellipse [cx, cy].
        h (float): mesh size.
        theta (float): rotation angle in radians.

    Outputs:
        mesh (MeshType): The mesh object created.
    """
    TITLE: str = "椭圆网格"
    PATH: str = "网格.构造"
    INPUT_SLOTS = [
        PortConf("mesh_type", DataType.MENU, 0, title="网格类型", default="tri", items=["tri", "quad"]),
        PortConf("a", DataType.FLOAT, 0, default=1.0, title="长轴"),
        PortConf("b", DataType.FLOAT, 0, default=1.0, title="短轴"),
        PortConf("x", DataType.FLOAT, 0, default=0.0, title="中心X坐标"),
        PortConf("y", DataType.FLOAT, 0, default=0.0, title="中心Y坐标"),
        PortConf("h", DataType.FLOAT, 0, default=0.1, title="网格尺寸"),
        PortConf("theta", DataType.FLOAT, 0, default=0.0, title="旋转角度(弧度)"),
    ]
    OUTPUT_SLOTS = [
        PortConf("mesh", DataType.MESH, title="网格"),
    ]
    
    @staticmethod
    def run(mesh_type, a, b, x, y, h, theta):
        from fealpy.mesher import EllipseMesher
        MeshClass = EllipseMesher()
        MeshClass.init_mesh.set(mesh_type)
        kwds = {"a": a, "b": b, "x": x, "y": y, "h": h, "theta": theta}
        return MeshClass.init_mesh(**kwds)