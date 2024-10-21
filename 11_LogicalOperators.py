#or and  not 
"""
temp = 20
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event is still scheduled")
"""

temp = 28
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside.")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is warm outside")
    print("It is sunny")


elif temp >= 28 and not is_sunny:
    print("It is hot outside.")
    print("It is cloudy")
elif temp <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is cloudy")
elif temp < 28 and temp > 0 and not is_sunny:
    print("It is warm outside")
    print("It is cloudy")

