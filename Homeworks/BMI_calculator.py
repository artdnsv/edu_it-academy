#Задание:
# 1. Запрашиваем входные данные
# 2. Считаем BMI по введенным параметрам
# 3. Выводим результат в виде текста - "Ваш индекс массы тела: <результат расчета>"
# 4. Выводим результат в виде шкалы: Пример: Если результат 30
#                                            20======|============50
#                                            Если 40
#
#                                            20============|======50

try:
    h = float(input('Введите ваш рост: '))
    th = input('Введите значение (см/м/фут):').lower()
    w = float(input('Введите ваш вес: '))
    tw = input('Введите значение (кг/фунт/стоун):').lower()
    if th == 'см':
        h /= 100
    elif th == 'фут':
        h *= 0.3048
    if tw == 'фунт':
        w *= 0.45359237
    elif tw == 'стоун':
        w *= 6.35029
    BMI = int(w / h ** 2)
    print(f'Ваш индекс массы тела: {BMI}')
    #от 20 до 50
    BMI_HI = 50
    BMI_LOW = 20
    width = 20
    percent = 0.2
    x = (BMI - BMI_LOW) / (BMI_HI - BMI_LOW)
    print('20' + '='*round(x*width) + '|' + '='*round((1-x)*width) + '50')
except ValueError:
    print('Неверное значение! Попробуйте снова')


