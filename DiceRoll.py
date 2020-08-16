import sys
import random
import re


def main(argv):
    if len(argv) > 2:
        usage(0)
    arg = argv[1]
    check(arg)
    dices = split(arg)
    check_digits(dices)
    dice_number = int(dices[0])
    dice_sides = int(dices[1])
    try:
        modificator = int(dices[2])
    except:
        modificator = 0
    rolls = []
    for result in dice_roll(dice_number, dice_sides, modificator):
        rolls.append(result)
    prntstr ='Your rolls: ' + '{}, '*dice_number + '\nSum of your rolls is: {}'
    print(prntstr.format(*rolls, sum(rolls)))


def check(arg):
    if 'd' not in arg:
        usage(0)
    if '.' in arg:
        usage(1)


def check_digits(arg):
    if '' in arg:
        usage(0)


def split(s):
    reg = re.split(r'\D+', s)
    return reg


def dice_roll(dices, sides, mod=0):  # generator
    i = 0
    while i < dices:
        i+=1
        x = random.randint(1, sides) + mod
        yield x


def usage(x = 0):
    if x == 0:
        print("Usage example: DiceRoll.py 2d4+1")
        sys.exit(0)
    if x == 1:
        print("Number of dices, sides and modificator must be INT.\nUsage example: DiceRoll.py 2d4+1")
        sys.exit(0)


if __name__ == '__main__':
    main(sys.argv)