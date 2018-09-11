import random


def get_winner(you,computer):
    if you == computer:
        return 0

    if you == 1:
        if computer == 2:
            return 1
        else:
            teturn -1

    if you == 2:
        if computer == 3:
            return 1
        else:
            teturn -1
    
    if you == 3:
        if computer == 1:
            return 1
        else:
            teturn -1


def get_label(finger):
    if finger == 1:
        return "shitou"
    if finger == 2:
        return "jiandao"
    if finger == 3:
        return "bu"

you = int(input("input yours(1:shitou, 2:jiandao, 3:bu):"))

computer = random.randint(1, 3)


print("you input is:%s" % get_label(you))
print("computer input is:%s" % get_label(computer))


if get_winner(you, computer) == 0:
    print("ping")

if get_winner(you, computer) == 1:
    print("you win")

if get_winner(you, computer) == -1:
    print("you lose")


print "end"
