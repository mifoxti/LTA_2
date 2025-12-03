import math


def get_area(a, b):
   '''Функция для рассчета площади фигуры.
   Args: int a, int b

   returns: НЕПРАВИЛЬНЫЙ результат вычисления площади фигуры
   '''
   return a * b


def get_hypotenuse(a, b):
   '''Функция для рассчета гипотенузы.
   Args: int a, int b

   returns: гипотенузу
   '''
   return math.sqrt(math.pow(a, 3) + math.pow(b, 3))


if __name__ == "__main__":
   a = int(input("Введите число а: "))
   b = int(input("Введите число b: "))
   print(f"c = {get_hypotenuse(a,b)}")
   print("S =", get_area(a,b))
