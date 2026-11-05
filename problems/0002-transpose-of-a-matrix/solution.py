def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    rows = len(a)
    cols = len(a[0])
    # print(a[0])
    res = []
    for j in range(cols):
        temp = []
        # print(temp)
        for i in range(rows):
            # print(f'adding {i, j}')
            temp.append(a[i][j])
        res.append(temp)
# [[00, 01, 02], [10, 11, 12]] -> [[00, 10], [01, 11], [02, 22] ]
# cols - 1 = 3 - 1 = 2
# rows - 1 = 2 -1 = 1
#  each prev col will be the j of the new rows
#  each prev col will be the i of the new column
    return res
