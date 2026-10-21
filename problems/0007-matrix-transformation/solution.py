import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A, T, S = (np.array(m, dtype=float) for m in (A, T, S))
	
	if abs(np.linalg.det(T)) < 1e-7 or abs(np.linalg.det(S)) < 1e-7:
		return -1

	return np.linalg.inv(T) @ A @ S