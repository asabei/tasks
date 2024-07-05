import sys
def generate_intervals(n, m):
  """
  Генерирует интервалы по круговому массиву с заданным интервалом.

  Args:
      n: Размер кругового массива.
      m: Длина интервала.

  Returns:
      Список интервалов.
  """
  intervals = []
  start = 1
  while True:
    interval = []
    for i in range(m):
      next_element = (start + i) % n
      if next_element == 0:
        next_element = n
      interval.append(next_element)
    intervals.append(interval)
    start = interval[-1]  # Устанавливаем последний элемент как новый start
    if start == 1:  # Цикл завершается, когда start становится равен 1
      break
  return intervals

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Неверное количество аргументов. Ожидается 2 аргумента: n m")
  else:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    intervals = generate_intervals(n, m)
    for interval in intervals:
      print(" ".join(str(x) for x in interval))
    path = [interval[0] for interval in intervals]
    print(" ".join(str(x) for x in path))
    
   