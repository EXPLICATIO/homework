# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def join_func(name, surname, year, city, email, telephone):
    try:
        name = input('Введит имя: ')
        surname = input('Введит фамилию: ')
        year = int(input('Введите Ваш год рождения: '))
        city = input('Введите Ваш город проживания: ')
        email = input('Введите Ваш  e-mail: ')
        telephone = int(input('Введите Ваш номер телефона: '))
    except ValueError:
        return


print(join_func(name = name, surname = surname,  year = year, city = city, email = email, telephone = telephone))
