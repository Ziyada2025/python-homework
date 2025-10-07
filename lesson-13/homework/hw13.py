from datetime import datetime, date, timedelta
asked=input('Enter your birtday(yyyy-mm-dd') 
year,month,day=asked.split('-') 
year=int(year) 
month=int(month) 
day=int(day) 
my_currentdate=datetime.today() 
t1=datetime(year=year, month=month, day=day) 
t2=(my_currentdate-t1)
print(f'You are lived {t2} days') 
year_t1=t1.year 
year_my_currentdate=my_currentdate.year 
t3=year_my_currentdate-year_t1 
print(f'You are {t3} year old') 
month_t1=t1.month 
month_my_currentdate=my_currentdate.month 
t4 = (year_my_currentdate - year_t1) * 12 + (month_my_currentdate - month_t1)
print(f'you are lived {t4} months')  
2.from datetime import datetime, date 
asked=input('Enter your birtday(yyyy-mm-dd)') 
year,month,day=asked.split('-') 
year=int(year) 
month=int(month) 
day=int(day)  
currentdate=datetime.today() 
t1=datetime(year=currentdate.year, month=month, day=day) 
if currentdate>t1:
    t1=datetime(year=currentdate.year+1, month=month, day=day) 
t2=t1-currentdate
print(f'There are {t2.days} days before your birthday')  
3.from datetime import datetime, date, time, timedelta
x=input('Enter your date and time of meeting here (yyyy-mm-dd HH:MM)') 
y=input('Enter duration of your meeting HH/MM')
date_part, time_part = x.split(' ')      # Split date and time
year, month, day = date_part.split('-')  # Split date part
hour, minute = time_part.split(':')   
hours, minutes = y.split('/') 
year = int(year)
month = int(month)
day = int(day)
hour = int(hour)
minute = int(minute)
hours = int(hours)
minutes = int(minutes)
beginning = datetime(year=year, month=month, day=day, hour=hour, minute=minute)
t1=beginning + timedelta(hours=hours, minutes=minutes) 
print(f'The meeting will be held on {x} and end at {t1}') 
4.from datetime import datetime, timezone
import pytz 
local_time=input("Enter here your local date and time (yyyy-mm-dd hh:mm)") 
desired_timezone=input("Enter here continent and city (continent/city)") 
date_part, date_time=local_time.split(' ') 
year, month, day=date_part.split('-') 
hour, minute=date_time.split(':') 
year = int(year)
month = int(month)
day = int(day)
hour = int(hour)
minute = int(minute) 
continent, cite=desired_timezone.split('/')
tz_NY=pytz.timezone(desired_timezone) 
datetime_NY=datetime.now(tz_NY)
print(f'Local time is {local_time} and your choosed timezone is {datetime_NY}') 
5.from datetime import datetime
import time

# Foydalanuvchidan kelajakdagi sana va vaqtni olish
target = input("Kiriting kelajakdagi sana va vaqt (YYYY-MM-DD HH:MM:SS): ")

# Matnni datetime obyektga aylantiramiz
target_time = datetime.strptime(target, "%Y-%m-%d %H:%M:%S")

print("\nTaymer ishga tushdi... ⏳\n")

# Har soniyada vaqtni tekshiramiz
while True:
    now = datetime.now()
    diff = target_time - now

    if diff.total_seconds() <= 0:
        print("\n⏰ Vaqt tugadi!")
        break

    # Kun, soat, daqiqa, soniya ajratish
    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    seconds = diff.seconds % 60

    # Natijani chiqarish (bitta satrda yangilanadi)
    print(f"\rQolgan vaqt: {days} kun {hours:02} soat {minutes:02} daqiqa {seconds:02} soniya", end="")

    # 1 soniya kutish
    time.sleep(1)

6.import re 
yourmail=input("Enter your email here:") 
pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  
if re.match(pattern, yourmail): 
    print('Your email is valid') 
else: 
    print('Your email not valid') 
7.yournumber=input('Enter your number here (xxxyyyzzdd)') 
formattednumber=f'({yournumber[:3]}) {yournumber[3:6]}-{yournumber[6:]}' 
print(f'Your number is {formattednumber}') 
8.import re

password = input("Enter your password: ")

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'

if re.match(pattern, password):
    print("Strong password")
else:
    print("Weak password") 
9.import re

text = "Python is amazing. I love learning Python because Python is powerful and easy to use."

word = input("Enter the word you want to find: ")

matches = re.findall(word, text, re.IGNORECASE)

print(f"The word '{word}' was found {len(matches)} times.") 
10.import re

text = input("Enter your text: ")

dates = re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}', text)

if dates:
    print("Dates found:", dates)
else:
    print("No dates found.")
