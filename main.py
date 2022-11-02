import random
import  sys
print("what your name")
username = input()
print("HI."+username)
print("do u want to play a game?(Yes or no)")
usersay = input()
while True:
    if str(usersay) != "yes" and str(usersay) != "Yes":
        sys.exit()
    else:
        print("go")
        break
print("take a nb dude")
nb = random.randint(1, 100)
for t in range(1, 16):
     print("the nb is on 1~20 you can try 15")
     yournb = int(input())
     if yournb > nb:
         print("you nb is too hight")
     elif yournb < nb:
         print("you nb is so low")
     else:
         break

if yournb == nb:
    print("you are good win!!")
elif yournb != nb:
    print("you are lose")

print("do u want to play next game?")
def ok (name):
    assert isinstance(name, object)
    print("next game is 11/8!!!"+name)


