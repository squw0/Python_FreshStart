#[start : end : step]

credit_card = "1234-5678-9012-3456"

#print(credit_card[0])
#print(credit_card[:4]) # Start pos 0 / End pos 4 / End digit is not printed
#print(credit_card[5:9])
#print(credit_card[5:]) # Start pos 5 / End pos last char
#print(credit_card[-1]) # Print last digit
#print(credit_card[::2]) # Everything from the begining to the end with Step = 2


#Find last 4 digits of credit card number
#last_digits = credit_card[-4:]
#print(f"XXXX-XXXX-XXXX-{last_digits}")


#Reverse numbers in credit card number
reverse = credit_card[::-1]
print(f"Your reversed credit card number is: {reverse}")
