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
5. Get the answer!

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


