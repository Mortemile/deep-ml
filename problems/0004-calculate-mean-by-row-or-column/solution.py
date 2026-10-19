def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'row':
		means = [sum(row)/len(row) for row in matrix]
	else:
		means = [sum(col)/len(col) for col in zip(*matrix)]
	return means