correct_birth_year = 1799
result = ''

while result != 'Верно':
    birth_year = int(input('Введите год рождения Пушкина:'))

    if birth_year == correct_birth_year:
        result = 'Верно'
    else:
        result = 'Неверно'

    print(result)
