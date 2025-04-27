def max_block_sum(input):
    matrix = input[0]
    block_height = input[1]
    block_width = input[2]

    max_sum = float('-inf')
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    for i in range(n_rows - block_height + 1):
        for j in range(n_cols - block_width + 1):
            current_sum = 0
            for k in range(block_height):
                for l in range(block_width):
                    current_sum += matrix[i + k][j + l]
            max_sum = max(max_sum, current_sum)

    return max_sum