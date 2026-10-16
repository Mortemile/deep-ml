def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here

    cols = len(a)
    rows = len(a[0])

    transposed = []
    for j in range(rows):
        new_row = []
        for i in range(cols):
            new_row.append(a[i].pop(0))
        transposed.append(new_row)
    return transposed