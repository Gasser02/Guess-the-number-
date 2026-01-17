#Guess the No game 


import random 

x =  random.randint(1,100)


while True :
    try:
        z = int(input("Guess a No. between 1 and 100 : "))
        if z == x :
            print("Gongrats you have guessed the No !!")
            break
        elif z > x :
            print("Too high")
        elif z < x :
            print("Too low")  
    except ValueError :
        print("enter No please ")     