
age = int(input("Enter your age: "))

if age >= 100:
    print("You're too old to sign up.")
elif age >= 18:
    print("You're now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up.")

####

response = input("Would you like food? (Y/N): ")
if response == "Y":
    print("Here is some food :)")
elif response != "Y" or response != "N":
    print("You've to type Y or N!")
else:
    print("No food for you!")

####

name = input("Enter your name: ")

if name == "":
    print("You did not type your name!!!")
else:
    print(f"Hello {name}!")


####

for_sale = True # False

if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale.")