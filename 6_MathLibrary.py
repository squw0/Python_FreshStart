import math

radius = float(input("Enter the radius of a circle (cm): "))

circumference = 2 * math.pi * radius # obwód koła 
#print(f"The circimference is: {circumference}")
print(f"The circimference is: {round(circumference, 2)}cm") # zaokrąglij do 2 miejsc po .

area = math.pi * pow(radius, 2) # ** 2 pole koła 
#print(f"The area of the circle is : {area}cm^2")
print(f"The area of the circle is: {round(area, 2)}cm^2")

####

a = float(input("Enter side A (cm): "))
b = float(input("Enter side B (cm): "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {c}cm")

####

x = 9.5

print(math.pi) # stała pi
print(math.e) # stała e

result = math.sqrt(x) # pierwiastek
print(result)

result1 = math.ceil(x) # zaokrąglenie w górę
print(result1)

result2 = math.floor(x) # zaokrąglenie w dół
print(result2)
