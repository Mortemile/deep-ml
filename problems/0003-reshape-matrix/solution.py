import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	new_rows, new_cols = new_shape
	rows, cols = len(a), len(a[0])

	if rows * cols != new_cols * new_rows:
		return []

	flat = [x for row in a for x in row]
	reshaped_matrix = [flat[i:i+cols] for i in range(0, len(flat), cols)]
	return reshaped_matrix