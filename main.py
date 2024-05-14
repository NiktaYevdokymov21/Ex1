import random

start = input('You`ce started the game "rock, paper". For the start press "+" or "-" for the end: ')

if start == '+':
    print('Loading...')
    print('Loading is finished! Let`s start the game!!')
    print('3...2...1...')
    print('If you want to exit press "-" ')
    print('Wanna know score? Press "?" ')
    user_ball = 0
    rand_ball = 0
    while True:
        user = input("Rock 'r', Paper 'p' or Scissors 's' ???\n")
        list_play = ["r", "p", "s"]
        if user in list_play:
            rand = random.choice(list_play)
            print(rand)

            if rand == 'r' and user == 's':
                rand_ball += 1
            if rand == 's' and user == 'p':
                rand_ball += 1
            if rand == 'p' and user == 's':
                rand_ball += 1
            if rand == 'r' and user == 'p':
                user_ball += 1
            if rand == 's' and user == 'r':
                user_ball += 1
            if rand == 'p' and user == 's':
                user_ball += 1
            if rand == user:
                pass
        elif user == "?":
            print(f'Your scores are {user_ball}. Scores of enemy are {rand_ball}.')
        elif user == "-":
            print(f'Your scores are {user_ball}. Scores of enemy are {rand_ball}.')
            print("Thanks for the game, see ya later")
        else:
            print('input: "r", "p", "s"  ')
if start == "-":
    print('So sad, se ya later...')
else:
    print('i didn`t understand you. Please restart the game.')
