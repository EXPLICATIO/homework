# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк
input_time = int(input('Введите время в секундах: '))
hours_count = input_time // 3600
minutes_count = (input_time - hours_count * 3600) // 60
seconds_count = input_time - hours_count * 3600 - minutes_count * 60
if input_time < 0:
    print('Время не может быть отрицательным!')
else:
    print(f'Время в в формате чч:мм:сс - {hours_count:02d}:{minutes_count:02d}:{seconds_count:02d}')
