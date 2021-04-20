import random

num = random.randint(0,2)

computer = ['rock','paper','scissor']

turn = computer[num]

player = False

while player == False:
    player=input('rock, paper or scissor? ')
    if player == turn:
        print('TIE!!')
    if player == 'rock':
        if turn == 'paper':
            print('you lose ', turn, ' covers ', player)
            break
        if turn == 'scissor':
            print('you win ', player, ' smashes ',turn)
    elif player == 'paper':
        if turn == 'scissor':
            print('you lose ', turn, " cuts ", player)
            break
        if turn == 'rock':
            print('you win ', player, ' covers ', turn)
    elif player == 'scissor':
        if turn == 'rock':
            print('you lose ', turn, ' smashes ', player)
            break
        if turn == 'paper':
            print('you win ', player, ' cuts ', turn)
    else:
        print('please enter a valid input')


    player = False
    turn = computer[num]