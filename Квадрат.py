#Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
#(с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

import math
def square(a):

    p = 4 * a
    s = a ** 2
    diag = a * math.sqrt(2)  # можно diag = math.hypot(a, a)

    return p, s, diag
print(square(9))