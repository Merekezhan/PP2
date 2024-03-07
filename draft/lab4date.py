"""Date
1 - Write a Python program to subtract five days from current date.
2 - Write a Python program to print yesterday, today, tomorrow.
3 - Write a Python program to drop microseconds from datetime.
4 - Write a Python program to calculate two date difference in seconds."""
#1
from datetime import datetime, timedelta
print("Current time: ", datetime.now())
print(datetime.now() - timedelta(days=5))

#2
from datetime import datetime, timedelta
print("Yesterday: ", datetime.now() - timedelta(days=1))
print("Current time: ", datetime.now())
print("Tomorrow: ", datetime.now() + timedelta(days=1))

#3
import datetime
print(datetime.datetime.today().replace(microsecond=0))

#4
import datetime as dt

a = dt.datetime(2024,2,21,21,45,45)
b = dt.datetime(2024,3,7,23,59,59)

print((b-a).total_seconds())
