import random
import time

# Конфігурація для 18 варіанта: (N, M, K, X_MIN, X_MAX)
CONFIG: tuple[int, int, int, int, int] = (21, 5, 3, 1, 99)


def generate_vector(length: int, min_val: int, max_val: int) -> list[int]:
	if length <= 0:
		raise ValueError("Довжина вектора має бути більшою за 0")
	if min_val > max_val:
		raise ValueError("Некоректні межі діапазону")

	return [random.randint(min_val, max_val) for _ in range(length)]


def compress_without_zeros(vector: list[int]) -> list[int]:
	# Стискаємо список через list comprehension, прибираючи всі нулі
	return [x for x in vector if x != 0]


def find_extremes(vector: list[int]) -> tuple[tuple[int, int], tuple[int, int]]:
	if not vector:
		raise ValueError("Вектор порожній")

	min_val = vector[0]
	max_val = vector[0]
	min_idx = 0
	max_idx = 0

	for i in range(1, len(vector)):
		if vector[i] < min_val:
			min_val = vector[i]
			min_idx = i
		if vector[i] > max_val:
			max_val = vector[i]
			max_idx = i

	# Повертаємо кортеж з (значення, індекс) для мінімуму і максимуму
	return (min_val, min_idx), (max_val, max_idx)


def selection_sort(vector: list[int]) -> list[int]:
	# Копіюємо список, щоб не змінити початковий вектор
	arr = list(vector)
	n = len(arr)

	for i in range(n - 1):
		min_idx = i
		for j in range(i + 1, n):
			if arr[j] < arr[min_idx]:
				min_idx = j

		# Міняємо елементи місцями без третьої змінної
		if min_idx != i:
			arr[i], arr[min_idx] = arr[min_idx], arr[i]

	return arr


def main() -> None:
	# Розпаковуємо параметри з незмінного кортежу
	n, m, k, x_min, x_max = CONFIG

	# Фіксуємо seed, щоб результати можна було повторити для звіту (можна закоментувати)
	random.seed(18)
	vector_v = generate_vector(n, x_min, x_max)

	print("=" * 80)
	print(f"{'ОБРОБКА ОДНОВИМІРНОГО ВЕКТОРА (ВАРІАНТ 18)':^80}")
	print("=" * 80)
	print(f"Параметри з CONFIG: N={n}, діапазон=[{x_min}, {x_max}] (M={m}, K={k})")
	print(f"Початковий вектор V:\n  {vector_v}")

	# Екстремуми
	(min_val, min_idx), (max_val, max_idx) = find_extremes(vector_v)
	print(f"Мінімальний елемент:  {min_val} (індекс {min_idx})")
	print(f"Максимальний елемент: {max_val} (індекс {max_idx})")

	# Стиснення вектора вилученням нулів
	compressed_v = compress_without_zeros(vector_v)
	removed_count = len(vector_v) - len(compressed_v)
	print(f"Після вилучення нулів (вилучено {removed_count} шт.):\n  {compressed_v}")

	# Оскільки в [1, 99] нулів немає, перевіряємо стиснення на контрольному прикладі
	test_with_zeros = [14, 0, 7, 0, 0, 53, 28, 0]
	print(f"Тест стиснення з нулями: {test_with_zeros} -> {compress_without_zeros(test_with_zeros)}")

	# Сортування вибором (без використання .sort())
	sorted_v = selection_sort(compressed_v)
	print(f"Відсортовано методом вибору (Selection Sort):\n  {sorted_v}")
	print("=" * 80)


if __name__ == "__main__":
	t_start = time.perf_counter()
	main()
	t_elapsed = (time.perf_counter() - t_start) * 1000
	print(f"Час виконання: {t_elapsed:.4f} мс\n")
