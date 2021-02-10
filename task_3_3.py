# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(arg1, arg2, arg3):
    """
    Функция описывает сравнение 3 чисел и сложение наибольших
    :param arg1: int
    :param arg2: int
    :param arg3: int
    :return: сумма наибольших двух
    """
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg2 < arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print(
    f'Сумма двух наибольших чисел равна:  {my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число:  ")))}')
