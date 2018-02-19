def count_holes(n):
    # переводимо в рядок (якщо це ще не рядок)
    n = str(n)
    # якщо число від'ємне, прибираємо мінус
    if n != '' and n[0] == '-':
        n = n[1:]
    # порожні значення виявились виключеннями
    if n is '':
        return 'ERROR'
    # оголошуємо словник із кількостями "отворів" - так буде зручніше рахувати
    hole_blueprint = {'0':1, '1':0, '2':0, '3':0, '4':1, '5':0, '6':1, '7':0, '8':2, '9':1}
    chars_allowed = hole_blueprint.keys()
    not_zero_chars = chars_allowed[:]
    not_zero_chars.remove('0')
    counter = 0
    # цю змінну використаємо, щоб пропустити зайві нулі на початку числа
    number_started = False
    # перебираємо розряди числа
    for char in n:
        # якщо натрапляємо на символ, відсутній в ключах словника, це не цифра, а все n - не ціле число
        if not(char in chars_allowed):
            return 'ERROR'
        # якщо поточний розряд не нуль, переключити змінну-флаг і можна починати рахувати "отвори"
        if char in not_zero_chars:
            number_started = True
        # якщо можна починати рахувати, додаємо до лічильника кількість "отворів" поточної цифри
        if number_started:
            counter = counter + int(hole_blueprint[char])
    if not number_started:
        counter = 1
    # повертаємо результат
    return counter