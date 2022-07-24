# rock paper scissors game:

import random


def rpsGame():
    print("'r' for rock, 'p' for paper, 's' for scissors")
    user = input('You: ')
    computer = random.choice(['r', 's', 'p'])
    print('Computer:', computer)
    if user == computer:
        return "draw!"
    # r>s, s>p, p>r
    if win(user, computer):
        return "You win!"
    return 'You lost!'

def win(player, computer):
    # r>s, s>p, p>r
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True
print(rpsGame())

