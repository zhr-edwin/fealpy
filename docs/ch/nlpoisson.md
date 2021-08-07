# 非线性 Poisson 方程求解

非线性方程在实际问题中经常出现，这里详细介绍求解非线性 Poisson
方程的典型方法，如

* Newton-Galerkin 方法
    - 先应用 Newton 方法线性化连续的弱形式，再用有限元离散次迭代求解
    - 先应用有限元离散连续的弱形式，再应用 Newton 方法迭代求解
* Picard 迭代方法
    - 又称定点迭代

## Newton-Galerkin 方法

首先给出一个扩散系数为非线性的例子

$$
-\nabla\left(a(u)\nabla u\right) = f
$$

满足如下的边界条件：

$$
u = g_D, \quad\text{on }\Gamma_D\leftarrow \text{\bf Dirichlet } 
$$

$$
\frac{\partial u}{\partial\bm n}  = g_N, \quad\text{on }\Gamma_N \leftarrow \text{\bf Neumann}
$$

$$
\frac{\partial u}{\partial\bm n} + \kappa u = g_R, \quad\text{on }\Gamma_R \leftarrow \text{\bf Robin}
$$

在 Poisson 方程两端分别乘以测试函数 $v \in H_{D,0}^1(\Omega)$, 利用分部积分，可得到其对应的**连续弱形式**

$$
(a(u)\nabla u,\nabla v)+<\kappa u,v>_{\Gamma_R} = (f,v)+<g_R,v>_{\Gamma_R}+<g_N,v>_{\Gamma_N}
$$

设 $u^0$ 是 $u$ 的一个逼近，记 $\delta u = u - u^0$, 代入连续弱形式

$$
(a(u^0+\delta u)\nabla (u^0+\delta u),\nabla v)+<\kappa u^0+\delta u, v>_{\Gamma_R} = (f,v)+<g_R,v>_{\Gamma_R}+<g_N,v>_{\Gamma_N}
$$

其中 $a(u^0+\delta u)$ 在 $u^0$ 处 Taylor 展开，可得

$$
a(u^0 + \delta u) = a(u^0) + a_u'(u^0)\delta u + \mathcal O(\delta u^2)
$$

替换连续弱形式中的 $a(u^0+\delta u)$, 并忽略掉其中 $\mathcal O(\delta u^2)$  可得

$$
(a(u^0)\nabla\delta u, \nabla v) + (a_u'(u^0)\nabla u^0\cdot\delta u, \nabla v) 
+ <\kappa\delta u, v>_{\Gamma_R}
=  (f,v) - (a(u^0)\nabla u^0, \nabla v) - <\kappa u^0, v>_{\Gamma_R} + <g_R,v>_{\Gamma_R}+<g_N,v>_{\Gamma_N}
$$

给定求解区域 $\Omega$ 上的网格离散 $\mathcal T = \{\tau\}$, 构造 $N$ 维的有限维空间 $V_h$，
其 $N$ 个**全局基函数**组成的**行向量函数**记为

$$
\bm\phi(\bm x) = \left[\phi_0(\bm x), \phi_1(\bm x), \cdots, \phi_{N-1}(\bm x)\right], \bm x \in \Omega 
$$

对于有限元程序设计实现来说，并不会显式构造出所谓的全局基函数，实际基函数的求值计
算都发生网格单元或网格单元的边界上。设每个网格单元 $\tau$ 上**局部基函数**个数为 
$l$ 个，其组成的**行向量函数**记为

$$
\bm\varphi(\bm x) = \left[\varphi_0(\bm x), \varphi_1(\bm x), \cdots, \varphi_{l-1}(\bm x)\right], \bm x \in \tau
$$

所有基函数梯度对应的向量

$$
\nabla \bm\varphi(\bm x) = \left[\nabla \varphi_0(\bm x), \nabla \varphi_1(\bm x), \cdots, \nabla \varphi_{l-1}(\bm x)\right], \bm x \in \tau
$$

其中 

$$
\nabla \varphi_i = \begin{bmatrix}
\frac{\partial \varphi_i}{\partial x_0} \\
\frac{\partial \varphi_i}{\partial x_1} \\
\vdots \\
\frac{\partial \varphi_i}{\partial x_{d-1}} \\
\end{bmatrix},
\quad i= 0, 1, \cdots, l-1.
$$


则 $(a(u^0)\nabla\delta u, \nabla v)$ 对应的单元矩阵为 

$$
\bm A_\tau = \int_\tau a(u^0)(\nabla \bm\varphi)^T\nabla\bm\varphi\mathrm d \bm x
$$

$(a_u'(u^0)\nabla u^0\cdot\delta u, \nabla v)$ 对应的单元矩阵为

$$
\bm B_\tau = \int_\tau a_u'(u^0)(\nabla\bm\varphi)^T\left(\nabla u^0\bm\varphi\right)\mathrm d \bm x
$$

$(f, v)$ 对应的单元列向量为

$$
\bm b = \int_\tau f\bm\varphi^T\mathrm d \bm x
$$

下面讨论边界条件相关的矩阵和向量组装。设网格边界边（2D)或边界面（3D)上的**局部基函数**个数为 $m$
个，其组成的**行向量函数**记为

$$
\bm\omega (\bm x) = \left[\omega_0(\bm x), \omega_1(\bm x), \cdots, \omega_{m-1}(\bm x)\right]
$$

设 $e$ 是一个边界边或边界面，则 $<\kappa\delta u, v>_e$ 对应的矩阵为

$$
\bm R_e = \int_e \kappa \bm\omega^T\bm\omega \mathrm d \bm s, \forall
e\subset\Gamma_R.
$$

$<g_N, v>_e$  对应的向量为

$$
\bm b_N = \int_e g_N\bm\omega^T\mathrm d \bm x, \forall e \subset \Gamma_N
$$

$<g_R, v>_e$ 对应的向量为

$$
\bm b_R = \int_e g_R\omega^T\mathrm d \bm x, \forall e \subset \Gamma_R 
$$

### 基于 FEALPy 的程序实现

设求解区域为 $\Omega=[0, 1]^2$ 真解设为

$$
u = \cos(\pi x)\cos(\pi y)
$$

非线性扩散系数设为

$$
a(u) = 1 + u^2
$$

边界条件设为纯 Dirichlet 边界条件，其线性化的连线弱形式为
$$
(a(u^0)\nabla\delta u, \nabla v) + (a_u'(u^0)\nabla u^0\cdot\delta u, \nabla v) 
=  (f,v) - (a(u^0)\nabla u^0, \nabla v)
$$

下面首先讨论模型数据代码实现


```python
import numpy as np
# 装饰子：指明被装饰函数输入的是笛卡尔坐标点
from fealpy.decorator import cartesian

@cartesian
def solution(p):
    # 真解函数
    pi = np.pi
    x = p[..., 0]
    y = p[..., 1]
    return np.cos(pi*x)*np.cos(pi*y)

@cartesian
def gradient(p):
    x = p[..., 0]
    y = p[..., 1]
    pi = np.pi
    val = np.zeros(p.shape, dtype=np.float64)
    val[..., 0] = -pi*np.sin(pi*x)*np.cos(pi*y)
    val[..., 1] = -pi*np.cos(pi*x)*np.sin(pi*y)
    return val # val.shape == p.shape

@cartesian
def source(p):
    x = p[..., 0]
    y = p[..., 1]
    pi = np.pi
    val = 2*pi**2*(3*np.cos(pi*x)**2*np.cos(pi*y)**2 - np.cos(pi*x)**2 - np.cos(pi*y)**2 + 1)*np.cos(pi*x)*cos(pi*y)
    return val

@cartesian
def dirichlet(p):
    return solution(p)
```

构造 $\Omega=[0, 1]^2$ 上的三角形网格，$x$ 和 $y$ 方向都剖分 10 段

```python
from fealpy.mesh import MeshFactory as MF
domain = [0, 1, 0, 1]
mesh = MF.boxmesh2d(domain, nx=10, ny=10, meshtype='tri')
```

构造 `mesh` 上的 $p$ 次 Lagrange 有限元空间 `space`, 并定义一个该空间的函数 `u0`,
其所有自由度默认为 0

```python
from fealpy.functionspace import LagrangeFiniteElementSpace

space = LagrangeFiniteElementSpace(mesh, p=1) # p=1 的线性元，
u0 = space.function()
du = space.function()
```

$(a_u'(u^0)\nabla u^0\cdot\delta u, \nabla v)$ 对应的组装代码

```python
# 装饰子：指明被装饰函数输入的是重心坐标点
from fealpy.decorator import barycentric 

@barycentric
def nlcoefficient(bc):
    '''
    u(bc) 的形状为 (NQ, NC)
    u.grad_value(bc) 的形状为 (NQ, NC, GD)

    两个数组相乘，需要在 u(bc) 的后面加一个轴
    '''
    return 2*u0(bc)[..., None]*u0.grad_value(bc)

def nolinear_matrix(space, c, q=3):
    mesh = space.mesh
    qf = mesh.integrator(q, 'cell') # 获得第 q 个积分公式
    bcs, ws = qf.get_quadrature_points_and_weights() # (NQ, TD+1) 获得积分点重心坐标和权重
    cellmeasure = mesh.entity_measure('cell') # (NC, )
    phi = space.basis(bcs) # (NQ, 1, dof) 获得每个单元基函数在积分点的值
    gphi = space.grad_basis(bcs) # （NQ, NC, ldof, GD), 获得每个单元基函数在重心坐标处的梯度值，
    val = c(bcs) # (NQ, NC, GD)

    # 组装单元矩阵， A.shape == (NC, ldof, ldof)
    B = np.einsum('q, qcid, qcd, qcj, c->cij', ws, gphi, val, phi, cellmeasure)
    gdof = space.number_of_global_dof() # 全局自由度的个数

    # (NC, ldof), cell2dof[i, j] 存储第 i 个单元上的局部第 j 个自由度的全局编号
    cell2dof = space.cell_to_dof()

    # (NC, ldof) --> (NC, ldof, 1) --> (NC, ldof, ldof)
    I = np.broadcast_to(cell2dof[:, :, None], shape=A.shape)

    # (NC, lodf) --> (NC, 1, ldof) --> (NC, ldof, ldof)
    J = np.broadcast_to(cell2dof[:, None, :], shape=A.shape)
    B = csr_matrix((B.flat, (I.flat, J.flat)), shape=(gdof, gdof))
    return 

```

下面边界条件处理与求解

```python
# 装饰子：指明被装饰函数输入的是重心坐标点
from fealpy.decorator import barycentric 
from fealpy.boundarycondition import DirichletBC
# solver
from scipy.sparse.linalg import spsolve


@barycentric
def dcoefficient(bcs):
    # 扩散系数
    return 1 + u0(bcs)**2

isDDof = space.set_dirichlet_bc(u0, dirichlet)
tol = 1e-8
b = space.source_vector(source)
while True:
    A = space.stiff_matrix(c=dcoefficient)
    B = nolinear_matrix(space)
    U = A + B
    F = b - A@u0
    du[isDDof] = spsolve(U[:, isDDof][isDDof, :], F[isDDof]).reshape(-1)
    u0[isDDof] += du
    if np.max(np.abs(du)) < tol:
        break
```











##  

第二个是反应项为非线性的例子

$$
-\nabla\left(\nabla u\right) + u^3=f 
$$


满足如下的边界条件：

$$
u = g_D, \quad\text{on }\Gamma_D\leftarrow \text{\bf Dirichlet } 
$$

$$
\frac{\partial u}{\partial\boldsymbol n}  = g_N, \quad\text{on }\Gamma_N \leftarrow \text{\bf Neumann}
$$

$$
\frac{\partial u}{\partial\boldsymbol n} + \kappa u = g_R, \quad\text{on }\Gamma_R \leftarrow \text{\bf Robin}
$$