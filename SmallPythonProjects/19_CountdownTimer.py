
import time

my_time = int(input("Enter the time in seconds: "))

# Counting 0 - my_time
#for x in range(0,my_time):
#    print(x)
#    time.sleep(1) #seconds


# Counting backwards because step is -1
#for x in range(my_time,0,-1):
#    print(x)
#    time.sleep(1) #seconds


for x in range(my_time,0,-1):
    seconds = x % 60 # cant go above 60
    minutes = int(x / 60) % 60 # 60 sec in minute + cant go above 60
    hours = int(x / 3600) # 3600 sec in hour // no % because there are no days
    print(f"{hours:02}:{minutes:02}:{seconds:02}") # 00:00:09  adds 0 before 9 and moves it 2 places right
    time.sleep(1) 


print("Time's up!")