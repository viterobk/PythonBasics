correct_birth_year = 1799
correct_birth_day = '6 июня'
birth_year = int(input('Введите год рождения Пушкина:'))

if birth_year != correct_birth_year:
    print('Неверный год рождения')
else:
    birth_day = input('Введите день рождения Пушкина:')

    if birth_day == correct_birth_day:
        print('Верно')
    else:
        print('Неверный день рождения')

