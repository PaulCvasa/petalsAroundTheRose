import random

def dice():
    face = [1, 2, 3, 4, 5, 6]
    petals=0
    d1 = random.choice(face)
    if d1==3:
        petals+=2
    elif d1==5:
        petals+=4
    dice_design(d1)
    d2 = random.choice(face)
    if d2==3:
        petals+=2
    elif d2==5:
        petals+=4
    dice_design(d2)
    d3 = random.choice(face)
    if d3==3:
        petals+=2
    elif d3==5:
        petals+=4
    dice_design(d3)
    d4 = random.choice(face)
    if d4==3:
        petals+=2
    elif d4==5:
        petals+=4
    dice_design(d4)
    d5 = random.choice(face)
    if d5==3:
        petals+=2
    elif d5==5:
        petals+=4
    dice_design(d5)
    p=input("x= ")
    p=int(p)
    petals=int(petals)
    if p==petals:
        print("---CORRECT---")
    else:
        print("---INCORRECT--- ANSWER: ",petals)

def dice_design(face):
    if face==1:
        print("+-------+")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print("+-------+")
    elif face==2:
        print("+-------+")
        print("| o     |")
        print("|       |")
        print("|     o |")
        print("+-------+")
    elif face==3:
        print("+-------+")
        print("| o     |")
        print("|   o   |")
        print("|     o |")
        print("+-------+")
    elif face==4:
        print("+-------+")
        print("| o   o |")
        print("|       |")
        print("| o   o |")
        print("+-------+")
    elif face==5:
        print("+-------+")
        print("| o   o |")
        print("|   o   |")
        print("| o   o |")
        print("+-------+")
    elif face==6:
        print("+-------+")
        print("| o   o |")
        print("| o   o |")
        print("| o   o |")
        print("+-------+")

ok=1
while(ok):
    dice()
    ok=input("Again? (0/1) ")
    ok=int(ok)