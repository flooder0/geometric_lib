## Наш проект - это калькулятор площади и периметра, который реализует функции по математическим формулам.

# Этот модуль позволяет вычислять площадь и периметр фигур (круга и квадрата) на основе пользовательского ввода.

Функция calc вычисляет значение заданной функции (площадь или периметр) для указанной фигуры (круг или квадрат) с использованием переданных размеров.

Параметры:
fig (str): Название фигуры, должно быть одним из значений в figs.
func (str): Название функции, должно быть одним из значений в funcs.
size (list): Список размеров, необходимых для вычисления (например, радиус для круга или длина стороны для квадрата).

Пример использования:

calc('circle', 'area', [5])  

# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer.

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

## Circle
Модуль для вычисления площади и периметра круга
Пример использования:

s = area(5)
print(s)  # Вывод: 78.53981633974483    

## Square
Модуль для вычисления площади и периметра квадрата

Пример использования:

s = area(4)
print(s)  # Вывод: 16.0

## Triangle
Модуль содержит функции для вычисления площади и периметра треугольника.

Пример использования:

p = area(3, 4, 5)
print(p)  # Вывод: 6.0


## Commits

b5b0fae727ca72c317c383b39c0af73d6adcd81c L-04: Update docs for calculate.py Tue Mar 30 18:02:23 2021 +0300
d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71 L-04: Add calculate.py Tue Mar 30 17:57:42 2021 +0300
51c40ebfd0e0b65f52fe5e54740cbb038e492db3 L-04: Doc updated for triangle Fri Mar 26 14:52:26 2021 +0300
d080c7888b81955bad2ed78d58ad910526b5132a L-04: Triangle added Fri Mar 26 14:48:39 2021 +0300
d078c8d9ee6155f3cb0e577d28d337b791de28e2 L-03: Docs added Thu Mar 4 14:55:29 2021 +0300
8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added Thu Mar 4 14:54:08 2021 +0300

