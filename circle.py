# Модуль для вычисления площади и периметра круга
import math

#Функция area вычисляет площадь круга, принимая радиус.
def area(r):
    return math.pi * r * r

#Параметры:
#r (float): Радиус круга.

#Возвращает:
#float: Площадь круга, которая равна π * r^2.

#Пример использования:

#s = area(5)
#print(s)  # Вывод: 78.53981633974483    


#Функция perimeter вычисляет периметр (длину окружности) круга, принимая радиус.
def perimeter(r):
    return 2 * math.pi * r


#Параметры:
#r (float): Радиус круга.

#Возвращает:
#float: Периметр круга, который равен 2 * π * r.
#Пример использования:

#p = perimeter(5)
#print(p)  # Вывод: 31.41592653589793