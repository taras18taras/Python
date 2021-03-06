import sys

a1 = int(sys.argv[1])
a2 = int(sys.argv[2])

# для найпростішої перевірки номерів будемо перетворювати числа на рядки, зберігаючи у цій змінній
i_str = ''
# власне лічильник "щасливих" номерів
counter = 0

# пробігаємо всі значення від а1 до а2
# для включення межевих значень цього другий аргумент range() необхідно задати на 1 більше
for i in range(a1, a2 + 1):
    # конвертуємо поточне число
    i_str = str(i)
    # визначаємо його довжину і кількість нулів, які слід додати
    zeros_to_add = 6 - len(i_str)
    # додаємо нулі до числа (арифметичні операції з рядками)
    i_str = zeros_to_add * '0' + i_str
    # порівнюємо суми цифр, для арифметичного додавання слід перевести цифри назад у числа
    # якщо суми дорівнюють, збільшуємо лічильник на 1
    if (int(i_str[0]) + int(i_str[1]) + int(i_str[2])) == (int(i_str[3]) + int(i_str[4]) + int(i_str[5])):
        counter = counter + 1

print(counter)
