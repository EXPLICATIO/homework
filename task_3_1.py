# Реализовать функцию, принимающую два числа(позиционные аргументы) и выполняющую их деление.\
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(*argument):
    """
    Функция делит два числа исключая деление на 0
    Используется глобальные аргменты для вывода
    :param argument: числа
    :return: деление чисел
    """
    global result, argument_1, agrument_2
    try:
        argument_1 = int(input("Введите делимое число: "))
        argument_2 = int(input("Введите делитель: "))
    except ValueError:
        return
    if argument_2 != 0:
        return argument_1 / argument_2
    else:
        print("На ноль делить нельзя!")
        exit()


print(div())
