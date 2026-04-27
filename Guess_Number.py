import random 
lucky_number=random.randint(1,100)
while True:
    num=int(input("Enter Your Number:"))
    if num==lucky_number:
        print("Congratulations!! You won the Game... 🎉")
        break
    elif num<lucky_number:
        print("Sorry!! You Number is Smaller than the Lucky Number")
    elif num>lucky_number:
        print("Sorry!! You Number is Greater than the Lucky Number")
    else:
        print("Invalid Number!!\nTry Again")