#name = input("Enter your full name: ")
#phone_number = input("Enter your phone #: ")



#result = len(name) #Counts length letters + digits + spaces etc
#result = name.find(" ") #Finds first occurence // position + no find == -1
#result = name.rfind(" ") #Finds last occurence couting from begining // position
#name = name.capitalize() #Capitalize first letter
#name = name.upper() #Capitalize all letters
#name = name.lower() #All letters are in lowercase
#result = name.isdigit() #Only digits + result is in Boolean 
#result = name.isalpha() #Only letters + no space etc
#result = phone_number.count("-") #Count something in ()
#phone_number = phone_number.replace("-", " ") #Replace something ("old", "new")



#print(phone_number)

#print(help(str)) #All methods

#Username (less than 12, no spaces, no digits)

username = input("Enter your username: ")

if len(username) > 12:
    print("No spaces, no digits, less than 12. Try again.")
elif not username.find(" ") == -1:
    print("No spaces, no digits, less than 12. Try again.")
elif not username.isalpha():
    print("No spaces, no digits, less than 12. Try again.")
else:
    print(f"Your username: {username} is amazing!")