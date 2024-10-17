# Этот модуль позволяет вычислять площадь и периметр фигур (круга и квадрата) на основе пользовательского ввода.

import circle #Модуль, содержащий функции для вычисления площади и периметра круга.

import square # Модуль, содержащий функции для вычисления площади и периметра квадрата.


## Переменные

figs = ['circle', 'square'] #Список доступных фигур. Включает `'circle'` и `'square'`.
funcs = ['perimeter', 'area'] #Список доступных функций. Включает `'perimeter'` и `'area'`.
sizes = {} #Словарь, который может использоваться для хранения количества параметров для каждой функции и фигуры.

'''
Функция calc вычисляет значение заданной функции (площадь или периметр) для указанной фигуры (круг или квадрат) с использованием переданных размеров.

Параметры:
fig (str): Название фигуры, должно быть одним из значений в figs.
func (str): Название функции, должно быть одним из значений в funcs.
size (list): Список размеров, необходимых для вычисления (например, радиус для круга или длина стороны для квадрата).

Пример использования:

calc('circle', 'area', [5])  

Вывод: area of circle is 78.53981633974483
'''

def calc(fig, func, size):
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



