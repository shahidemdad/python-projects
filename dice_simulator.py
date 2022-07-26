'''
Dice Simulator:
    we will build a rolled dice system terminal based simulator.

    Algorithm:
        1. dice
        2. capture a random number 1-6
        3. simulate

'''
import random

#random values 1-6
def randomNum():
    dice_num = random.randint(1,6)
    return caseViews(dice_num) 

#cases
def caseViews(dice_num):
    if dice_num == 1:
        print("--------")
        print("|      |")
        print("|   0  |")
        print("|      |")
        print("--------")
    if dice_num == 2:
        print("--------")
        print("|      |")
        print("| 0  0 |")
        print("|      |")
        print("--------")
    if dice_num == 3:
        print("--------")
        print("|      |")
        print("| 0  0 |")
        print("|   0  |")
        print("--------")
    if dice_num == 4:
        print("--------")
        print("| 0  0 |")
        print("|      |")
        print("| 0  0 |")
        print("--------")
    if dice_num == 5:
        print("--------")
        print("| 0  0 |")
        print("|   0  |")
        print("| 0  0 |")
        print("--------")
    if dice_num == 6:
        print("--------")
        print("| 0  0 |")
        print("| 0  0 |")
        print("| 0  0 |")
        print("--------")

#main
def main():
    text_input = input("r for roll, x for no: ")
    if text_input == "r":
        randomNum()
main()