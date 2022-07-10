from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time of alarm to be set(hour:minute:second:period):")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[4:6]
alarm_seconds = alarm_time[8:10]
alarm_period = alarm_time[12:14].upper()
print("Setting up alarm")

flag = True
while flag:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if current_hour == alarm_hour and current_minute == alarm_minute and current_seconds == alarm_seconds:
        print("Wake Up!")
        playsound('audio.mp3')
        flag = False
