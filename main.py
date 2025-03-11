import unittest

def zigzag_traversal(matrix):
    if not matrix or not matrix[0]:
        return []
    
    m, n = len(matrix), len(matrix[0])
    result = []
    diagonals = [[] for _ in range(m + n - 1)]
    
    for i in range(m):
        for j in range(n):
            diagonals[i + j].append(matrix[i][j])
    
    for index, diag in enumerate(diagonals):
        if index % 2 == 0:
            result.extend(diag[::-1]) 
        else:
            result.extend(diag)
    
    return result

