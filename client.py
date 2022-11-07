# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».

from engine import guess_a_number, check_number
import engine as en
import os

player_number = ''

guess_a_number()
turn = 0
bulls = cows = 0
while True:
    turn += 1
    player_number = input('Ваше число: ')
    scores = check_number(player_number=player_number)
    print('= Быков {}, коров {} ='.format(scores['bulls'], scores['cows']))
    if scores['bulls'] == 4:
        print('=== Число компьютера: {} ==='.format(en.computer_number))
        print('=== Вы прошли игру за {} ходов! ==='.format(turn))
        new_game = input('Хотите сыграть еще? [1/0]: ')
        if new_game == '1':
            # os.system('CLS')
            guess_a_number()
        else:
            break