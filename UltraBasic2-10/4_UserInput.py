age = int(input("What is your age?: "))
name = input("What is your name?: ")

print(f"Hello {name}!!!!")
print(f"You're {age} years old")

age = age + 1 
print(f"You'll be {age} years old next year")

###

length = float(input("Insert length in cm: "))
width = float(input("Insert width in cm: "))

print("\nLets calculate rectangle area!\n")
area = length * width
print(f"The area of rectangle is {area}cm^2, length = {length}, width = {width}")

###

item = input("What item would you like to buy?: ")
price = float(input("What is the price in $?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"\nYou've bought {quantity} X {item}/s! \nTotal price is: ${total}")