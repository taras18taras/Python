input_list = [1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]
def clean_list(list_to_clean):
    # Тут будуть зберігатися знайдені унікальні значення
    found = []
    # Перевіряємо елементи отриманого списку
    for element in list_to_clean:
        # Спочатку вважаємо поточний елемент "новим"
        flag = False
        # Перевіряємо вже знайдені значення
        for i in found:
            # Якщо елемент вже є у списку знайдених
            if i == element and str(i) == str(element):
                # Значить він не "новий"
                flag = True
        # Якщо "новий", то додати до списку знайдених значень
        if not flag:
            found.append(element)
    # Повернути список
    return found
print(clean_list(input_list))
