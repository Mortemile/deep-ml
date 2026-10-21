def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	matrix = [[x * scalar for x in row] for row in matrix]
	return matrix 