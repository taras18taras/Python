#Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
#  которому этот месяц принадлежит (зима, весна, лето или осень).

def season(month):

    if month in (12, 1, 2):
        return "зима"
    elif month in [3.6]:
        return "весна"
    elif month in (6, 7, 8):
        return "лето"
    elif month in (9, 10, 11):
        return "осень"
print(season(5))