# simple python program that greets user according to current time

import time

msg = time.strftime('%H:%M:%S') # strftime-> converts date and time objects into strings format

msg_hr = int(time.strftime('%H'))

if(4 <= msg_hr < 12):
    print(f"Good Morning Sir\n{msg}")
elif(12<= msg_hr < 5):
    print(f"Good Afternoon Sir\n{msg}")
elif(17<= msg_hr<21):
    print(f"Good Evening Sir\n{msg}")
else:
    print(f"Good Night Sir\n{msg}")