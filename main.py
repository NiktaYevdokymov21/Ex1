import random

start = input('Ви почали гру «Камінь, папір». Для початку натисніть "+" або "-" для кінця: ')

if start == '+':
    print('Завантаження...')
    print('Завантаження завершено! Давайте почнемо гру!!')
    print('3...2...1...')
    print('Якщо ви хочете вийти, натисніть "-" ')
    print('Хочете знати рахунок? Прес "?" ')
    user_ball = 0
    rand_ball = 0
    while True:
        user = input("Камінь 'r', папір 'p' або ножиці 's' ???\n")
        list_play = ["r", "p", "s"]
        if user in list_play:
            rand = random.choice(list_play)
            print(rand)

            if rand == 'r' and user == 's':
                rand_ball += 1
                print('Ви програєте')
            if rand == 's' and user == 'p':
                rand_ball += 1
                print('Ви програєте')
            if rand == 'p' and user == 'r':
                rand_ball += 1
                print('Ви програєте')
            if rand == 'r' and user == 'p':
                user_ball += 1
                print('Ти виграв')
            if rand == 's' and user == 'r':
                user_ball += 1
                print('Ти виграв')
            if rand == 'p' and user == 's':
                user_ball += 1
                print('Ти виграв')
            if rand == user:
                print('Нічия')
        elif user == "?":
            print(f'Ваші бали {user_ball}. Бали ворога є {rand_ball}.')
        elif user == "-":
            print(f'Ваші бали {user_ball}. Бали ворога є {rand_ball}.')
            print("Дякую за гру, побачимося пізніше")
        else:
            print('input: "r", "p", "s"  ')
if start == "-":
    print('Сумно, побачимося пізніше...')
else:
    print('Я тебе не зрозумів. Перезапустіть гру.')
