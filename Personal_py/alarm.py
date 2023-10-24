import time
from playsound import playsound

# A list to store multiple alarm times
alarm_times = []

def get_valid_alarm_time():
    while True:
        try:
            alarm_time = input("Enter the alarm time in HH:MM format or 'exit' to stop: ")
            if alarm_time.lower() == 'exit':
                return None
            alarm_hour, alarm_minute = map(int, alarm_time.split(":"))

            if 0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59:
                return alarm_hour, alarm_minute
            else:
                print("Invalid time format. Please use HH:MM format.")
        except ValueError:
            print("Invalid input. Please use HH:MM format.")

def set_alarm(alarm_hour, alarm_minute):
    try:
        while True:
            current_time = time.localtime()
            current_seconds = current_time.tm_hour * 3600 + current_time.tm_min * 60 + current_time.tm_sec
            alarm_seconds = alarm_hour * 3600 + alarm_minute * 60
            seconds_until_alarm = alarm_seconds - current_seconds

            if seconds_until_alarm <= 0:
                print("It's time!")
                playsound("alarm_sound.mp3")
                break

            time.sleep(1)

    except KeyboardInterrupt:
        print("Alarm clock stopped.")

# Main loop
while True:
    alarm_time = get_valid_alarm_time()
    if alarm_time is None:
        break  # Exit if 'exit' is entered

    alarm_times.append(alarm_time)
    alarm_times.sort()  # Sort alarms in chronological order

    print(f"Alarm set for {alarm_time[0]:02d}:{alarm_time[1]:02d}")

# Set and trigger the alarms
for alarm_time in alarm_times:
    set_alarm(alarm_time[0], alarm_time[1])
