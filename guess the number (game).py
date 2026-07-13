# guess the number game
import random 
secret_number=random.randint(1,10)
guess=int(input("enter a number(1 to 10):"))
print(secret_number)
if guess==secret_number:
    print("you won!")
else:
    print("try again")
    
