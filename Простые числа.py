#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
# если оно простое, и False - иначе
def is_prime(number):
    """Эту функцию можно сильно оптимизировать. Подумайте, как"""

    if number == 1:
        return False  # 1 - не простое число

    for possible_divisor in range(2, number):
        if number % possible_divisor == 0:
            return False

    return True
print(is_prime(10000000001))