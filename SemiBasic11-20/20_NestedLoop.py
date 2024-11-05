
# repeat y loop 3 times
#for x in range(3): # (3) == (1,4)
#    for y in range(1,10): # prints 1-9
#        print(y,end=" ") # end="\n" new row for each // end="" same line for all
#    print() # prints new line


# draw rectangle 
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows): 
    for y in range(columns): 
        print(symbol,end=" ") 
    print() 

