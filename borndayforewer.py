correct_birth_year = 1799
correct_birth_day = '6 июня'
is_year_correct = False
is_day_correct = False

while not is_year_correct:
    birth_year = int(input('Введите год рождения Пушкина:'))

    if birth_year == correct_birth_year:
        is_year_correct = True
    else:
        print('Неверный день рождения')


while not is_day_correct:
    birth_day = input('Введите день рождения Пушкина:')

    if birth_day == correct_birth_day:
        print('Верно')
        is_day_correct = True
    else:
        print('Неверный день рождения')