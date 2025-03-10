import numpy as np

# 定义多个典型的 BDMDof 对象
# TetrahedronMesh.from_box(nx = 1,ny =1,nz=1)
# p =  3

init_data = [
    {
        "cdof":60,
        "gdof":300,
        "cell2dof":np.array([[ 80,  82,  81,  92,  85,  84,  94,  83, 114,  95,  89,  88,  97,
         87, 174,  98,  86, 118, 117,  99,  90,  91, 112, 111,  93, 180,
        181, 115, 182, 113,  96, 171, 172, 173, 183, 175, 119, 177, 178,
        116, 110, 184, 185, 186, 187, 188, 189, 190, 191, 192, 170, 193,
        194, 195, 196, 197, 176, 198, 199, 179],
       [ 70,  72,  71, 102,  75,  74, 104,  73,  94, 105,  79,  78, 107,
         77, 164, 108,  76,  97,  98, 109, 100, 101,  91,  92, 103, 200,
        201,  93, 202,  95, 106, 161, 162, 163, 203, 165,  96, 167, 168,
         99,  90, 204, 205, 206, 207, 208, 209, 210, 211, 212, 160, 213,
        214, 215, 216, 217, 166, 218, 219, 169],
       [ 10,  12,  11,  22,  15,  14,  24,  13, 104,  25,  19,  18,  27,
         17, 134,  28,  16, 107, 108,  29,  20,  21, 101, 102,  23, 220,
        221, 103, 222, 105,  26, 131, 132, 133, 223, 135, 106, 137, 138,
        109, 100, 224, 225, 226, 227, 228, 229, 230, 231, 232, 130, 233,
        234, 235, 236, 237, 136, 238, 239, 139],
       [  0,   2,   1,  62,   5,   4,  64,   3,  24,  65,   9,   8,  67,
          7, 124,  68,   6,  27,  28,  69,  60,  61,  21,  22,  63, 240,
        241,  23, 242,  25,  66, 121, 122, 123, 243, 125,  26, 127, 128,
         29,  20, 244, 245, 246, 247, 248, 249, 250, 251, 252, 120, 253,
        254, 255, 256, 257, 126, 258, 259, 129],
       [ 30,  32,  31,  52,  35,  34,  54,  33,  64,  55,  39,  38,  57,
         37, 144,  58,  36,  67,  68,  59,  50,  51,  61,  62,  53, 260,
        261,  63, 262,  65,  56, 141, 142, 143, 263, 145,  66, 147, 148,
         69,  60, 264, 265, 266, 267, 268, 269, 270, 271, 272, 140, 273,
        274, 275, 276, 277, 146, 278, 279, 149],
       [ 40,  42,  41, 111,  45,  44, 114,  43,  54, 113,  49,  48, 118,
         47, 154, 117,  46,  57,  58, 116, 110, 112,  51,  52, 115, 280,
        281,  53, 282,  55, 119, 151, 152, 153, 283, 155,  56, 157, 158,
         59,  50, 284, 285, 286, 287, 288, 289, 290, 291, 292, 150, 293,
        294, 295, 296, 297, 156, 298, 299, 159]], dtype=np.int32),
    
    "basis_vector":np.array([[[-1.        , -1.        , -1.        ],
        [ 0.        , -1.        , -1.        ],
        [-0.        ,  0.        , -1.        ],
        [-0.47140452, -0.47140452,  0.94280904],
        [-0.        , -1.        , -1.        ],
        [ 0.        ,  0.        , -1.        ],
        [-0.        , -0.70710678,  0.70710678],
        [-0.        , -0.        , -1.        ],
        [ 0.        ,  1.41421356,  0.        ],
        [ 0.        ,  0.        ,  1.41421356],
        [-1.41421356, -1.41421356, -0.        ],
        [ 0.        , -1.41421356, -0.        ],
        [-0.70710678,  0.70710678,  0.        ],
        [-0.94280904,  0.47140452,  0.47140452],
        [-0.        , -1.41421356, -0.        ],
        [ 1.        , -0.        , -0.        ],
        [ 1.        ,  0.        , -0.        ],
        [ 0.        ,  1.41421356,  0.        ],
        [ 1.        ,  1.        , -0.        ],
        [ 0.        ,  1.41421356,  1.41421356],
        [-1.41421356, -0.        , -0.        ],
        [ 1.        ,  0.        ,  0.        ],
        [ 0.70710678,  0.70710678,  0.        ],
        [ 0.57735027,  0.57735027,  0.57735027],
        [ 1.        ,  0.        ,  0.        ],
        [ 0.        ,  1.        ,  0.        ],
        [ 0.        ,  0.70710678,  0.70710678],
        [ 1.        ,  1.        ,  0.        ],
        [ 0.        ,  0.        ,  1.        ],
        [ 1.        ,  1.        ,  1.        ]],

       [[-1.        , -1.        , -1.        ],
        [ 0.        , -1.        ,  0.        ],
        [ 0.        , -1.        , -1.        ],
        [-0.94280904,  0.47140452,  0.47140452],
        [-0.        , -1.        , -0.        ],
        [ 0.        , -1.        , -0.        ],
        [-0.        , -0.        ,  1.41421356],
        [-0.        , -1.        , -1.        ],
        [-0.        , -0.70710678,  0.70710678],
        [ 0.        ,  1.41421356,  1.41421356],
        [-1.41421356, -0.        , -0.        ],
        [-0.70710678, -0.        ,  0.70710678],
        [-0.        , -0.        ,  1.41421356],
        [ 0.47140452, -0.94280904,  0.47140452],
        [-0.        , -0.        ,  1.41421356],
        [ 1.        ,  0.        ,  0.        ],
        [ 1.        , -0.        ,  1.        ],
        [-0.        , -0.        ,  1.41421356],
        [ 1.        ,  0.        , -0.        ],
        [-0.        , -1.41421356, -0.        ],
        [ 1.41421356,  0.        ,  1.41421356],
        [ 0.70710678,  0.        ,  0.70710678],
        [ 1.        ,  0.        ,  0.        ],
        [ 0.57735027,  0.57735027,  0.57735027],
        [ 1.        ,  0.        ,  1.        ],
        [ 0.        ,  0.        , -1.        ],
        [ 0.        ,  1.        ,  0.        ],
        [ 1.        ,  0.        ,  0.        ],
        [ 0.        ,  0.70710678,  0.70710678],
        [ 1.        ,  1.        ,  1.        ]],

       [[-1.        , -1.        , -1.        ],
        [-1.        , -1.        ,  0.        ],
        [ 0.        , -1.        ,  0.        ],
        [-0.47140452,  0.94280904, -0.47140452],
        [-1.        , -1.        , -0.        ],
        [ 0.        , -1.        ,  0.        ],
        [-0.70710678,  0.70710678, -0.        ],
        [-0.        , -1.        , -0.        ],
        [-1.41421356, -0.        , -0.        ],
        [ 0.        ,  1.41421356,  0.        ],
        [-1.41421356, -0.        , -1.41421356],
        [-1.41421356, -0.        ,  0.        ],
        [-0.70710678, -0.        ,  0.70710678],
        [-0.47140452, -0.47140452,  0.94280904],
        [-1.41421356, -0.        , -0.        ],
        [-0.        , -0.        ,  1.        ],
        [ 0.        , -0.        ,  1.        ],
        [-1.41421356, -0.        , -0.        ],
        [ 1.        , -0.        ,  1.        ],
        [-1.41421356, -1.41421356, -0.        ],
        [ 0.        ,  0.        ,  1.41421356],
        [ 0.        ,  0.        ,  1.        ],
        [ 0.70710678,  0.        ,  0.70710678],
        [ 0.57735027,  0.57735027,  0.57735027],
        [ 0.        ,  0.        ,  1.        ],
        [ 1.        ,  0.        ,  0.        ],
        [ 0.70710678,  0.70710678,  0.        ],
        [ 1.        ,  0.        ,  1.        ],
        [ 0.        ,  1.        ,  0.        ],
        [ 1.        ,  1.        ,  1.        ]],

       [[-1.        , -1.        , -1.        ],
        [-1.        ,  0.        ,  0.        ],
        [-1.        , -1.        ,  0.        ],
        [ 0.47140452,  0.47140452, -0.94280904],
        [-1.        , -0.        , -0.        ],
        [-1.        , -0.        ,  0.        ],
        [-0.        ,  1.41421356, -0.        ],
        [-1.        , -1.        , -0.        ],
        [-0.70710678,  0.70710678, -0.        ],
        [ 1.41421356,  1.41421356,  0.        ],
        [-0.        , -0.        , -1.41421356],
        [-0.        ,  0.70710678, -0.70710678],
        [-0.        ,  1.41421356, -0.        ],
        [-0.94280904,  0.47140452,  0.47140452],
        [-0.        ,  1.41421356, -0.        ],
        [ 0.        ,  0.        ,  1.        ],
        [-0.        ,  1.        ,  1.        ],
        [-0.        ,  1.41421356, -0.        ],
        [ 0.        , -0.        ,  1.        ],
        [-1.41421356, -0.        , -0.        ],
        [ 0.        ,  1.41421356,  1.41421356],
        [ 0.        ,  0.70710678,  0.70710678],
        [ 0.        ,  0.        ,  1.        ],
        [ 0.57735027,  0.57735027,  0.57735027],
        [ 0.        ,  1.        ,  1.        ],
        [ 0.        , -1.        ,  0.        ],
        [ 1.        ,  0.        ,  0.        ],
        [ 0.        ,  0.        ,  1.        ],
        [ 0.70710678,  0.70710678,  0.        ],
        [ 1.        ,  1.        ,  1.        ]],

       [[-1.        , -1.        , -1.        ],
        [-1.        ,  0.        , -1.        ],
        [-1.        ,  0.        ,  0.        ],
        [ 0.94280904, -0.47140452, -0.47140452],
        [-1.        , -0.        , -1.        ],
        [-1.        ,  0.        ,  0.        ],
        [ 0.70710678, -0.        , -0.70710678],
        [-1.        , -0.        , -0.        ],
        [-0.        , -0.        , -1.41421356],
        [ 1.41421356,  0.        ,  0.        ],
        [-0.        , -1.41421356, -1.41421356],
        [-0.        ,  0.        , -1.41421356],
        [-0.        ,  0.70710678, -0.70710678],
        [-0.47140452,  0.94280904, -0.47140452],
        [-0.        , -0.        , -1.41421356],
        [-0.        ,  1.        , -0.        ],
        [-0.        ,  1.        ,  0.        ],
        [-0.        , -0.        , -1.41421356],
        [-0.        ,  1.        ,  1.        ],
        [-1.41421356, -0.        , -1.41421356],
        [ 0.        ,  1.41421356,  0.        ],
        [ 0.        ,  1.        ,  0.        ],
        [ 0.        ,  0.70710678,  0.70710678],
        [ 0.57735027,  0.57735027,  0.57735027],
        [ 0.        ,  1.        ,  0.        ],
        [ 0.        ,  0.        ,  1.        ],
        [ 0.70710678,  0.        ,  0.70710678],
        [ 0.        ,  1.        ,  1.        ],
        [ 1.        ,  0.        ,  0.        ],
        [ 1.        ,  1.        ,  1.        ]],

       [[-1.        , -1.        , -1.        ],
        [-0.        ,  0.        , -1.        ],
        [-1.        ,  0.        , -1.        ],
        [-0.47140452,  0.94280904, -0.47140452],
        [-0.        , -0.        , -1.        ],
        [-0.        ,  0.        , -1.        ],
        [-1.41421356,  0.        ,  0.        ],
        [-1.        , -0.        , -1.        ],
        [ 0.70710678, -0.        , -0.70710678],
        [-1.41421356, -0.        , -1.41421356],
        [ 0.        ,  1.41421356,  0.        ],
        [-0.70710678,  0.70710678,  0.        ],
        [ 1.41421356, -0.        , -0.        ],
        [ 0.47140452,  0.47140452, -0.94280904],
        [-1.41421356,  0.        ,  0.        ],
        [ 0.        ,  1.        ,  0.        ],
        [ 1.        ,  1.        , -0.        ],
        [ 1.41421356, -0.        , -0.        ],
        [-0.        ,  1.        ,  0.        ],
        [-0.        , -0.        , -1.41421356],
        [ 1.41421356,  1.41421356,  0.        ],
        [ 0.70710678,  0.70710678,  0.        ],
        [ 0.        ,  1.        ,  0.        ],
        [ 0.57735027,  0.57735027,  0.57735027],
        [ 1.        ,  1.        ,  0.        ],
        [-1.        ,  0.        ,  0.        ],
        [ 0.        ,  0.        ,  1.        ],
        [ 0.        ,  1.        ,  0.        ],
        [ 0.70710678,  0.        ,  0.70710678],
        [ 1.        ,  1.        ,  1.        ]]],dtype=np.float64),
    
    "basis":np.array([[[[-0.1       , -0.1       , -0.1       ],
         [-0.        , -0.3       , -0.3       ],
         [-0.        , -0.        , -0.1       ],
         [ 0.        ,  0.        ,  0.70710678],
         [-0.14142136, -0.14142136, -0.        ],
         [-0.        , -0.42426407, -0.        ],
         [ 0.        ,  0.14142136,  0.        ],
         [ 0.        ,  0.70710678,  0.70710678],
         [-0.14142136, -0.        , -0.        ],
         [ 0.3       ,  0.        ,  0.        ],
         [ 0.1       ,  0.1       ,  0.        ],
         [ 0.5       ,  0.5       ,  0.5       ]],

        [[-0.2       , -0.2       , -0.2       ],
         [-0.        , -0.2       , -0.2       ],
         [-0.        , -0.        , -0.2       ],
         [ 0.        ,  0.        ,  0.56568542],
         [-0.28284271, -0.28284271, -0.        ],
         [-0.        , -0.28284271, -0.        ],
         [ 0.        ,  0.28284271,  0.        ],
         [ 0.        ,  0.56568542,  0.56568542],
         [-0.28284271, -0.        , -0.        ],
         [ 0.2       ,  0.        ,  0.        ],
         [ 0.2       ,  0.2       ,  0.        ],
         [ 0.4       ,  0.4       ,  0.4       ]]],


       [[[-0.1       , -0.1       , -0.1       ],
         [-0.        , -0.3       , -0.        ],
         [-0.        , -0.1       , -0.1       ],
         [ 0.        ,  0.70710678,  0.70710678],
         [-0.14142136, -0.        , -0.        ],
         [-0.        , -0.        ,  0.42426407],
         [-0.        , -0.        ,  0.14142136],
         [-0.        , -0.70710678, -0.        ],
         [ 0.14142136,  0.        ,  0.14142136],
         [ 0.3       ,  0.        ,  0.3       ],
         [ 0.1       ,  0.        ,  0.        ],
         [ 0.5       ,  0.5       ,  0.5       ]],

        [[-0.2       , -0.2       , -0.2       ],
         [-0.        , -0.2       , -0.        ],
         [-0.        , -0.2       , -0.2       ],
         [ 0.        ,  0.56568542,  0.56568542],
         [-0.28284271, -0.        , -0.        ],
         [-0.        , -0.        ,  0.28284271],
         [-0.        , -0.        ,  0.28284271],
         [-0.        , -0.56568542, -0.        ],
         [ 0.28284271,  0.        ,  0.28284271],
         [ 0.2       ,  0.        ,  0.2       ],
         [ 0.2       ,  0.        ,  0.        ],
         [ 0.4       ,  0.4       ,  0.4       ]]],


       [[[-0.1       , -0.1       , -0.1       ],
         [-0.3       , -0.3       , -0.        ],
         [-0.        , -0.1       , -0.        ],
         [ 0.        ,  0.70710678,  0.        ],
         [-0.14142136, -0.        , -0.14142136],
         [-0.42426407, -0.        , -0.        ],
         [-0.14142136, -0.        , -0.        ],
         [-0.70710678, -0.70710678, -0.        ],
         [ 0.        ,  0.        ,  0.14142136],
         [ 0.        ,  0.        ,  0.3       ],
         [ 0.1       ,  0.        ,  0.1       ],
         [ 0.5       ,  0.5       ,  0.5       ]],

        [[-0.2       , -0.2       , -0.2       ],
         [-0.2       , -0.2       , -0.        ],
         [-0.        , -0.2       , -0.        ],
         [ 0.        ,  0.56568542,  0.        ],
         [-0.28284271, -0.        , -0.28284271],
         [-0.28284271, -0.        , -0.        ],
         [-0.28284271, -0.        , -0.        ],
         [-0.56568542, -0.56568542, -0.        ],
         [ 0.        ,  0.        ,  0.28284271],
         [ 0.        ,  0.        ,  0.2       ],
         [ 0.2       ,  0.        ,  0.2       ],
         [ 0.4       ,  0.4       ,  0.4       ]]],


       [[[-0.1       , -0.1       , -0.1       ],
         [-0.3       , -0.        , -0.        ],
         [-0.1       , -0.1       , -0.        ],
         [ 0.70710678,  0.70710678,  0.        ],
         [-0.        , -0.        , -0.14142136],
         [-0.        ,  0.42426407, -0.        ],
         [-0.        ,  0.14142136, -0.        ],
         [-0.70710678, -0.        , -0.        ],
         [ 0.        ,  0.14142136,  0.14142136],
         [ 0.        ,  0.3       ,  0.3       ],
         [ 0.        ,  0.        ,  0.1       ],
         [ 0.5       ,  0.5       ,  0.5       ]],

        [[-0.2       , -0.2       , -0.2       ],
         [-0.2       , -0.        , -0.        ],
         [-0.2       , -0.2       , -0.        ],
         [ 0.56568542,  0.56568542,  0.        ],
         [-0.        , -0.        , -0.28284271],
         [-0.        ,  0.28284271, -0.        ],
         [-0.        ,  0.28284271, -0.        ],
         [-0.56568542, -0.        , -0.        ],
         [ 0.        ,  0.28284271,  0.28284271],
         [ 0.        ,  0.2       ,  0.2       ],
         [ 0.        ,  0.        ,  0.2       ],
         [ 0.4       ,  0.4       ,  0.4       ]]],


       [[[-0.1       , -0.1       , -0.1       ],
         [-0.3       , -0.        , -0.3       ],
         [-0.1       , -0.        , -0.        ],
         [ 0.70710678,  0.        ,  0.        ],
         [-0.        , -0.14142136, -0.14142136],
         [-0.        , -0.        , -0.42426407],
         [-0.        , -0.        , -0.14142136],
         [-0.70710678, -0.        , -0.70710678],
         [ 0.        ,  0.14142136,  0.        ],
         [ 0.        ,  0.3       ,  0.        ],
         [ 0.        ,  0.1       ,  0.1       ],
         [ 0.5       ,  0.5       ,  0.5       ]],

        [[-0.2       , -0.2       , -0.2       ],
         [-0.2       , -0.        , -0.2       ],
         [-0.2       , -0.        , -0.        ],
         [ 0.56568542,  0.        ,  0.        ],
         [-0.        , -0.28284271, -0.28284271],
         [-0.        , -0.        , -0.28284271],
         [-0.        , -0.        , -0.28284271],
         [-0.56568542, -0.        , -0.56568542],
         [ 0.        ,  0.28284271,  0.        ],
         [ 0.        ,  0.2       ,  0.        ],
         [ 0.        ,  0.2       ,  0.2       ],
         [ 0.4       ,  0.4       ,  0.4       ]]],


       [[[-0.1       , -0.1       , -0.1       ],
         [-0.        , -0.        , -0.3       ],
         [-0.1       , -0.        , -0.1       ],
         [-0.70710678, -0.        , -0.70710678],
         [ 0.        ,  0.14142136,  0.        ],
         [-0.42426407,  0.        ,  0.        ],
         [ 0.14142136, -0.        , -0.        ],
         [-0.        , -0.        , -0.70710678],
         [ 0.14142136,  0.14142136,  0.        ],
         [ 0.3       ,  0.3       ,  0.        ],
         [ 0.        ,  0.1       ,  0.        ],
         [ 0.5       ,  0.5       ,  0.5       ]],

        [[-0.2       , -0.2       , -0.2       ],
         [-0.        , -0.        , -0.2       ],
         [-0.2       , -0.        , -0.2       ],
         [-0.56568542, -0.        , -0.56568542],
         [ 0.        ,  0.28284271,  0.        ],
         [-0.28284271,  0.        ,  0.        ],
         [ 0.28284271, -0.        , -0.        ],
         [-0.        , -0.        , -0.56568542],
         [ 0.28284271,  0.28284271,  0.        ],
         [ 0.2       ,  0.2       ,  0.        ],
         [ 0.        ,  0.2       ,  0.        ],
         [ 0.4       ,  0.4       ,  0.4       ]]]],dtype=np.float64),

    "div_basis":np.array([[[ 1.        ,  1.        ,  1.        ,  1.41421356,
          1.41421356,  1.41421356,  1.41421356,  1.41421356,
          1.41421356,  1.        ,  1.        ,  1.        ],
        [ 1.        ,  1.        ,  1.        ,  1.41421356,
          1.41421356,  1.41421356,  1.41421356,  1.41421356,
          1.41421356,  1.        ,  1.        ,  1.        ]],

       [[ 1.        ,  1.        ,  1.        ,  1.41421356,
          1.41421356,  1.41421356, -1.41421356, -1.41421356,
         -1.41421356,  1.        ,  1.        ,  1.        ],
        [ 1.        ,  1.        ,  1.        ,  1.41421356,
          1.41421356,  1.41421356, -1.41421356, -1.41421356,
         -1.41421356,  1.        ,  1.        ,  1.        ]],

       [[ 1.        ,  1.        ,  1.        ,  1.41421356,
          1.41421356,  1.41421356, -1.41421356, -1.41421356,
         -1.41421356,  1.        ,  1.        ,  1.        ],
        [ 1.        ,  1.        ,  1.        ,  1.41421356,
          1.41421356,  1.41421356, -1.41421356, -1.41421356,
         -1.41421356,  1.        ,  1.        ,  1.        ]],

       [[ 1.        ,  1.        ,  1.        ,  1.41421356,
          1.41421356,  1.41421356, -1.41421356, -1.41421356,
         -1.41421356,  1.        ,  1.        ,  1.        ],
        [ 1.        ,  1.        ,  1.        ,  1.41421356,
          1.41421356,  1.41421356, -1.41421356, -1.41421356,
         -1.41421356,  1.        ,  1.        ,  1.        ]],

       [[ 1.        ,  1.        ,  1.        ,  1.41421356,
          1.41421356,  1.41421356, -1.41421356, -1.41421356,
         -1.41421356,  1.        ,  1.        ,  1.        ],
        [ 1.        ,  1.        ,  1.        ,  1.41421356,
          1.41421356,  1.41421356, -1.41421356, -1.41421356,
         -1.41421356,  1.        ,  1.        ,  1.        ]],

       [[ 1.        ,  1.        ,  1.        , -1.41421356,
         -1.41421356, -1.41421356, -1.41421356, -1.41421356,
         -1.41421356,  1.        ,  1.        ,  1.        ],
        [ 1.        ,  1.        ,  1.        , -1.41421356,
         -1.41421356, -1.41421356, -1.41421356, -1.41421356,
         -1.41421356,  1.        ,  1.        ,  1.        ]]],dtype=np.float64),
    }
]