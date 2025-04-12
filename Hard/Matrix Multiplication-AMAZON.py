import numpy as np

def pad_kernel(kernel, image_shape):
    _kernel = np.array(kernel)

    padded_kernel = [[0 for _ in range(image_shape[1] - 1 + _kernel.shape[1])] for _ in range(image_shape[0] - 1 + _kernel.shape[0])]
    for i in range(_kernel.shape[0]):
        for j in range(_kernel.shape[1]):
            padded_kernel[i][j] = kernel[i][j]
    return padded_kernel

def toeplitz(c, r):
    n = len(c)
    m = len(r)
    toeplitz_matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i - j >= 0:
                toeplitz_matrix[i][j] = c[i - j]
            else:
                toeplitz_matrix[i][j] = r[j - i]
    return toeplitz_matrix

def create_block_matrix(toeplitz_matrices, di):
    h, w = len(toeplitz_matrices[0]), len(toeplitz_matrices[0][0])
    di_h, di_w = len(di), len(di[0])
    block_matrix = [[0 for _ in range(w * di_w)] for _ in range(h * di_h)]

    for i in range(di_h):
        for j in range(di_w):
            i0 = i * h
            j0 = j * w
            i1 = i0 + h
            j1 = j0 + w
            matrix_index = int(di[i][j]) - 1
            for mi in range(h):
                for mj in range(w):
                    block_matrix[i0 + mi][j0 + mj] = toeplitz_matrices[matrix_index][mi][mj]
    return block_matrix

def conv_2d_matrix_mult(input):
    image = input["image"]
    kernel = input["kernel"]
    
    assert len(image) == len(image[0])
    assert len(kernel) == len(kernel[0])

    padded_kernel = pad_kernel(kernel, (len(image), len(image[0])))

    toeplitz_matrices = []
    for i in range(len(padded_kernel) - 1, -1, -1):
        c = padded_kernel[i]
        r = [c[0]] + [0] * (len(image[0]) - 1)
        toeplitz_matrices.append(toeplitz(c, r))
    
    c = list(range(1, len(padded_kernel) + 1))
    r = [c[0]] + [0] * (len(image) - 1)
    di = toeplitz(c, r)
    
    block_matrix = create_block_matrix(toeplitz_matrices, di)
    
    flatten_image = [item for sublist in reversed(image) for item in sublist]
    
    result = []
    for row in block_matrix:
        result.append(sum(a*b for a, b in zip(row, flatten_image)))
    
    result_matrix = []
    res_height = len(image) + len(kernel) - 1
    res_width = len(image[0]) + len(kernel[0]) - 1
    for i in range(res_height):
        result_matrix.append(result[i * res_width: (i + 1) * res_width])
    
    return result_matrix