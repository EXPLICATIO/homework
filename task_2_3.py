# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons = {"Зима": (1, 2, 12), 'Весна': (3, 4, 5), "Лето": (6, 7, 8), 'Осень': (9, 10, 11)}
month_number = int(input('Введите номер месяца от 1 до 12 включительно: '))
if month_number > 12 or month_number < 1:
    print('Вы ввели неверное значение!')
for key in seasons.keys():
    if month_number in seasons[key]:
        print(key)
winter_list = [1, 2, 12]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
autumn_list = [9, 10, 11]
