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
        user = input("Rock, Paper or Scissors")
        list_play = ["r", "p", "s"]