def dfsComponentSize(matrix, vertex):
    return matrix[vertex].count(True) + 1
