# format specifiers = {value:flags} format a value based on what flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator


price1 = 3.14159
price2 = -987.65
price3 = 1200.34

#print(f"Price 1 is ${price1:.1f}") # round to that many decimal places (fixed point)
#print(f"Price 1 is ${price1:10}") # allocate and zero pad that many spaces $   3.14159 (10 spaces long)
#print(f"Price 1 is ${price1:010}") # $0003.14159 (10 spaces long)
#print(f"Price 1 is ${price1:<10}") # $3.14159 left justify
#print(f"Price 1 is ${price1:>10}") # $   3.14159 right justify
#print(f"Price 1 is ${price1:^10}") # $ 3.14159 centered
#print(f"Price 1 is ${price1:+}") # $+3.14159 but $-987.65 doesn't change
#print(f"Price 1 is ${price1: }") # insert a space before positive numbers
#print(f"Price 3 is ${price3:,}") # $1,200.34 comma separator
print(f"Price 1 is ${price1:+,.2f}") # $+3.14
