import sys
import math

def calculate_point_position(x_center, y_center, radius, x_point, y_point):
  """
  Рассчитывает положение точки относительно окружности.

  Args:
      x_center: Координата X центра окружности.
      y_center: Координата Y центра окружности.
      radius: Радиус окружности.
      x_point: Координата X точки.
      y_point: Координата Y точки.

  Returns:
      0 - точка лежит на окружности
      1 - точка внутри
      2 - точка снаружи
  """
  distance = math.sqrt((x_point - x_center) ** 2 + (y_point - y_center) ** 2)
  if abs(distance - radius) < 1e-6:  # Проверка на равенство с учетом погрешности
    return 0
  elif distance < radius:
    return 1
  else:
    return 2

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Неверное количество аргументов. Ожидается 2 аргумента: путь к файлу 1, путь к файлу 2")
    sys.exit(1)

  file_circle = sys.argv[1]
  file_points = sys.argv[2]

  with open(file_circle, "r") as f:
    x_center, y_center, radius = map(float, f.read().split())

  with open(file_points, "r") as f:
    for line in f:
      x_point, y_point = map(float, line.split())
      position = calculate_point_position(x_center, y_center, radius, x_point, y_point)
      print(position)