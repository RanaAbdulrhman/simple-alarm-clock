#! python3
""" A Simple Python script to set an alarm for a specific time.
    The program takes the date and time from the command-line
    When the alarm goes off, an alerting sound is played
"""

import subprocess
import time
import datetime
import sys


def get_date_time():
    """gets the date and time from command-line arguments"""
    if len(sys.argv) < 2:
        print("Usage:: enter 'python alarm_clock.py YEAR/MONTH/DAY HOUR:MIN:SEC' e.g. 2021/5/21 7:30:0 ")
    elif len(sys.argv) == 3:
        arguments = " ".join(sys.argv[1:])
        date, time = arguments.split(" ")
        year,month,day = date.split("/")
        hour,min,seconds = time.split(":")
        return year,month,day,hour,min,seconds
    elif len(sys.argv) == 2:
        print("number of arguments provided is not enough")
    elif len(sys.argv) > 3:
        print("number of arguments provided is too much")
    sys.exit()


def get_time_left_until(year, month, day, hour, min, sec):
    """ Measure the number of hours, minutes, and seconds - left until a certain date and returns the values."""
    now = datetime.datetime.now()
    aim = datetime.datetime(year, month, day, hour, min, sec)
    time_left = aim - now   # returns a timedelta object
    total_seconds = time_left.seconds
    hours = total_seconds // 3600
    minutes = (total_seconds - (hours * 3600)) // 60
    seconds = total_seconds - (minutes * 60)
    return hours, minutes, seconds


year, month, day, hour, min, seconds = get_date_time()   # get date and time from command-line arguments
print(f"""Your alarm is set
On date {year}/{month}/{day} at {hour}:{min}:{seconds}, the alarm will go off.""")

while True:
    hoursLeft, minLeft, secondsLeft = get_time_left_until(int(year), int(month), int(day), int(hour), int(min), int(seconds)) # get time left for the alarm to go off
    if hoursLeft == 0 and minLeft == 0:
        if secondsLeft == 0:
            print("\nIT'S TIME!")
            print("ToTaToTaToTa")
            subprocess.Popen([r'C:\Program Files\Windows Media Player\wmplayer.exe', r'C:\SOUND\FILE\PATH\IN\YOUR\COMPUTER\alarm.wav'])
            break
        if secondsLeft <= 10:
            print(f"{secondsLeft}..")  # display time left just in the last 10 seconds
            time.sleep(1)


