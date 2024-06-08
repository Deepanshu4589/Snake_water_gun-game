import random

list_comp = ["Snake", "Water", "Gun"]
Comp = random.choice(list_comp)

try :
    print(" Snake Water Gun")
    Player = input("Enter your choice:").capitalize()
    print(Comp)

except Exception:
    print("""In put is not valid,  so..... 
    sorry you lose""")
    exit()

if Player == Comp:
    print("Match Draw")

elif(Player == "Snake" and Comp == "Water"):
    print("You Win....")

elif(Player == "Water" and Comp == "Gun"):
    print("You Win....")

elif(Player == "Gun" and Comp == "Snake"):
        print("You Win....")

else:
    print("You Lose")

