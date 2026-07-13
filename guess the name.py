# guess the name 
import random
friends=["bala","tharun","changal","durga","vamsi"]
secret_name=random.choice(friends)
guess=input("enter a guess name from friends:")
print(secret_name)
if guess==secret_name:
    print("you won")
else:
    print("try again")
    
    