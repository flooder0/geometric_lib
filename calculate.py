
import circle #Модуль, содержащий функции для вычисления площади и периметра круга.

import square # Модуль, содержащий функции для вычисления площади и периметра квадрата.



figs = ['circle', 'square'] #Список доступных фигур. Включает `'circle'` и `'square'`.
funcs = ['perimeter', 'area'] #Список доступных функций. Включает `'perimeter'` и `'area'`.
sizes = {} #Словарь, который может использоваться для хранения количества параметров для каждой функции и фигуры.


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



