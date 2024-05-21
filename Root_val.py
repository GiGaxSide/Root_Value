"""

Made by GiGaSidexSuryansh to calculate the infinite decimal places of Root Numbers #1

"""
from decimal import Decimal, getcontext
import sys
import time
import os

getcontext().prec = 5 #Define it your self as it defines the number of decmial places that will come on starting
Clear_Screen = False

def Findirrational(x):
    global Clear_Screen
    if Clear_Screen == False:
        os.system('cls' if os.name == 'nt' else 'clear')
        Clear_Screen = True
    elif Clear_Screen == True:
        sys.stdout.write("\x1b[2J\x1b[H" + str(x)) 
        sys.stdout.flush()
        time.sleep(0.01) #Define it Your self as it defines the time. It is by default in seconds, here it is in 0.01 seconds

while True:
    try:
        User = input("\nEnter the number of which you want to calculate the root: ")
        if not User.strip():
            print("\nExiting...")
            exit()
        elif User.startswith("E") or User.startswith("e"):
            print("\nExiting...")
            exit()
        Power = input("\nEnter the power of the root(For example: For square root its 1/2 and for cube root its 1/3): 1/")
    except KeyboardInterrupt:
        print('\nExiting...')
        exit()
    if User.isdigit() and int(User) > 0 and Power.isdigit() and int(Power) > 0:
        const = int(User)
        Num = Decimal(User)
        Power_Num = Decimal(Power)
        while True:
            try:
                getcontext().prec += 1  #Define it your self as it defines that how the decimal places will come means one after one or two after two
                Num = (1/Power_Num) * ((Power_Num - 1) * Num + const / Num**(Power_Num-1))
                Findirrational(Num)
            except KeyboardInterrupt:
                print(f"\nThe number in root was {User} and the power of root was 1/{Power}")
                Clear_Screen = False
                break
    elif User.startswith('e') or Power.startswith("e") or not Power.strip():
        print("\nExiting...")
        exit()
    else:
        print("\nPlease enter a natural number in both the root number and its power.")
        Clear_Screen = False
