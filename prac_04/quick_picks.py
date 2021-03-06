import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    no_quick_picks = int(input("How many quick picks would you like? "))
    while no_quick_picks < 0:
        print("Does not compute! Please pick a number greater than 0 (zero)")
        no_quick_picks = int(input("How many quick picks would you like? "))

    for a in range(no_quick_picks):
        quick_pick = []
        for b in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()