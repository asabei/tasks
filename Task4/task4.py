import sys

def min_moves(nums):
    """
    Вычисляет минимальное количество ходов для приведения всех элементов массива к одному числу.

    Args:
        nums: Список целых чисел.

    Returns:
        Минимальное количество ходов.
    """
    if not nums:
        return 0

    total_sum = sum(nums)
    target_value = total_sum // len(nums)
    total_moves = 0
    for num in nums:
        total_moves += abs(num - target_value)

    return total_moves

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Пожалуйста, укажите путь к файлу с числами как аргумент командной строки.")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as file:
            nums_str = file.read().strip()
            nums = list(map(int, nums_str.split()))
            min_moves_count = min_moves(nums)
            print(f"Минимальное количество ходов: {min_moves_count}")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")

