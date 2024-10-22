# X if condition else Y 

num = 6 
a = 6
b = 7
age = 15
temperature = 20
user_role = "guest"

#print("Possitive" if num > 0 else "Negative")
#result = "Even" if num % 2 == 0 else "Odd"
#max_num = a if a > b else b
#min_num = a if a < b else b
#status = "Adult" if age >= 18 else "Child"
#weather = "Hot" if temperature > 20 else "Cold"
access_level = "Full access" if user_role == "admin" else "Limited access"

print(access_level)