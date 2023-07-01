data = [
    {
        'name': 'Ивана Грозного',
        'birth_year': 1530
    },
    {
        'name': 'Михаила Ломоносова',
        'birth_year': 1711
    },
    {
        'name': 'Дмитрия Менделеева',
        'birth_year': 1834
    },
    {
        'name': 'Юрия Гагарина',
        'birth_year': 1934
    },
    {
        'name': 'Льва Яшина',
        'birth_year': 1929
    }
]

lets_continue = True

while lets_continue:
    correct_answers = 0
    for item in data:
        # Правильные ответы:
        # - Ивана Грозный: 1530
        # - Михаил Ломоносов: 1711
        # - Дмитрий Менделеев: 1834
        # - Юрий Гагарин: 1934
        # - Лев Яшин: 1929
        year = int(input('Введите год рождения ' + item['name'] + ': '))
        if year == item['birth_year']:
            correct_answers += 1

    incorrect_answers = len(data) - correct_answers
    print('Количество правильных ответов:', correct_answers)
    print('Количество ошибок:', incorrect_answers)
    print('% правильных ответов:', int(correct_answers / len(data) * 100), '%')
    print('% ошибок:', int(incorrect_answers / len(data) * 100), '%')

    answer = input('Попробуем еще раз? да/нет: ')
    if answer != 'да':
        lets_continue = False
