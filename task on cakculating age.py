input("enter your name:")
birth_year=int(input("enter your birthday year:"))
print("Hello Blasri ")
import datetime
now=datetime.datetime.now()
age=now.year-birth_year
print("your age is:",age)
print("Today's Date:",now.strftime("%d-%m-%Y"))
print("Current Time:",now.strftime("%H-%M-%S"))

