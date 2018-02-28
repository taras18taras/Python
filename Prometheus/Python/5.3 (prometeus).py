def super_fibonacci(n, m):
    # за умовою перші m елементів - одиниці
    if n<=m:
        return 1
    # інакше доведеться рахувати
    else:
        # ініціалізуємо змінну для суми
        sum = 0
        # і додаємо m попередніх членів послідовності, для розрахунку кожного з них рекурсивно викликаємо нашу функцію
        for i in range(1, m+1):
            previous = super_fibonacci(n-i, m)
            sum = sum + previous
        # повертаємо суму, яка є значенням n-го елементу
        return sum
print(super_fibonacci(21,2))