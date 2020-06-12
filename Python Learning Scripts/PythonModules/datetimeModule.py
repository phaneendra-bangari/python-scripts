#Some important usage of datetime modules
from datetime import *
import pytz

print(datetime.now()) #Displays the date and time completely.
print(datetime.today()) #Displays the date and time.

IST_TIMEZONE=pytz.timezone('Asia/Kolkata')
print(datetime.now(IST_TIMEZONE)) #You cannot use today() like this.

#Fromtimestamp returns the time from 1970-01-01 05:30:00 to the number of seconds we add as input. 
print(datetime.fromtimestamp(86400)) # 86400 is the number of seconds per day.i
print(datetime.fromtimestamp(0))
