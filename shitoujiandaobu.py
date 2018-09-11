import random


user = int(input("please input(1:shitou, 2:jiandao, 3:bu):"))
print("your inout:%d"% user)
computer = random.randint(1,3)

print("computer input:%d"% computer) 

if (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
    print("goog job")

elif (user == 1 and computer == 1) or (user == 2 and computer == 2) or (user == 3 and computer == 3):
    print("ping")
else:
    print("you lose")
