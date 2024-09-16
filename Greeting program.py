import time

current_hour= time.strftime('%H')
if (int(current_hour)<12) :
    print("Good Morning Sir!")
elif (int(current_hour)<17) :
    print("Good Afternoon Sir!")
else:
    print("Good Evening Sir!")
    