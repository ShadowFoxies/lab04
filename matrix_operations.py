import random
import time

# Конфігурація для 18 варіанта: (N, M, K, X_MIN, X_MAX)
CONFIG: tuple[int, int, int, int, int] = (21, 5, 3, 1, 99)


def generate_matrix(rows: int, cols: int, min_val: int, max_val: int) -> list[list[int]]:
	if rows <= 0 or cols <= 0:
		raise ValueError("Розміри матриці мають бути більшими за 0")
	return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def sort_rows_by_sum(matrix: list[list[int]]) -> list[list[int]]:
	# Копіюємо рядки і сортуємо їх за зростанням суми елементів у рядку
	return [list(row) for row in sorted(matrix, key=sum)]


def multiply_matrices(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
	rows_a = len(matrix_a)
	cols_a = len(matrix_a[0])
	rows_b = len(matrix_b)
	cols_b = len(matrix_b[0])

	if cols_a != rows_b:
		raise ValueError(f"Матриці не сумісні для множення: {rows_a}x{cols_a} та {rows_b}x{cols_b}")

	# Класичне множення матриць C = A * B
	result = [
		[
			sum(matrix_a[i][k] * matrix_b[k][j] for k in range(cols_a))
			for j in range(cols_b)
		]
		for i in range(rows_a)
	]
	return result


def find_saddle_points(matrix: list[list[int]]) -> list[tuple[int, int, int]]:
	rows = len(matrix)
	cols = len(matrix[0])
	saddle_points = []

	row_mins = [min(row) for row in matrix]
	col_maxs = [max(matrix[r][c] for r in range(rows)) for c in range(cols)]

	for i in range(rows):
		for j in range(cols):
			val = matrix[i][j]
			if val == row_mins[i] and val == col_maxs[j]:
				saddle_points.append((i, j, val))

	return saddle_points


def print_matrix(matrix: list[list[int]], title: str, show_sums: bool = False) -> None:
	print(f"\n--- {title} ({len(matrix)}x{len(matrix[0])}) ---")
	for row in matrix:
		row_str = " ".join(f"{elem:6d}" for elem in row)
		if show_sums:
			print(f"  [ {row_str} ]  | сума = {sum(row)}")
		else:
			print(f"  [ {row_str} ]")


def main() -> None:
	# Розпаковуємо параметри з конфігураційного кортежу
	n, m, k, x_min, x_max = CONFIG

	random.seed(18)

	print("=" * 80)
	print(f"{'МАТРИЧНА АЛГЕБРА ТА ПОШУК СІДЛОВИХ ТОЧОК (ВАРІАНТ 18)':^80}")
	print("=" * 80)
	print(f"Параметри з CONFIG: A({m}x{k}), B({k}x{k}), діапазон=[{x_min}, {x_max}] (N={n})")

	# 1. Генерація матриці A (5x3) і перестановка рядків за сумою
	mat_a = generate_matrix(m, k, x_min, x_max)
	print_matrix(mat_a, "Початкова матриця A", show_sums=True)

	mat_a_sorted = sort_rows_by_sum(mat_a)
	print_matrix(mat_a_sorted, "Матриця A (рядки за зростанням сум)", show_sums=True)

	# 2. Генерація сумісної матриці B (3x3) і множення A * B
	mat_b = generate_matrix(k, k, x_min, x_max)
	print_matrix(mat_b, "Сумісна матриця B")

	mat_c = multiply_matrices(mat_a, mat_b)
	print_matrix(mat_c, "Добуток C = A x B")

	# 3. Пошук сідлових точок у матриці A
	saddles_a = find_saddle_points(mat_a)
	print("\nСідлові точки у матриці A:")
	if saddles_a:
		for idx, (r, c, val) in enumerate(saddles_a, start=1):
			print(f"  Точка {idx}: рядок={r}, стовпець={c}, значення={val}")
	else:
		print("  У згенерованій матриці A сідлових точок немає.")

	# Контрольний тест пошуку сідлових точок на фіксованій матриці
	test_matrix = [
		[4, 9, 5],
		[2, 7, 1],
		[6, 8, 5],
	]
	print_matrix(test_matrix, "Контрольна матриця для перевірки сідлових точок")
	saddles_test = find_saddle_points(test_matrix)
	print("Результати на контрольній матриці:")
	for idx, (r, c, val) in enumerate(saddles_test, start=1):
		print(f"  Точка {idx}: рядок={r}, стовпець={c}, значення={val}")

	print("=" * 80)


if __name__ == "__main__":
	t_start = time.perf_counter()
	main()
	t_elapsed = (time.perf_counter() - t_start) * 1000
	print(f"Час виконання: {t_elapsed:.4f} мс\n")
