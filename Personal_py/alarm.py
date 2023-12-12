import time
from playsound import playsound

def get_valid_alarm_time():
    while True:
        try:
            alarm_time = input("Enter the alarm time in HH:MM format or 'exit' to stop: ")
            if alarm_time.lower() == 'exit':
                return None
            alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
            if 0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59:
                return alarm_hour, alarm_minute
            print("Invalid time format. Please use HH:MM format.")
        except ValueError:
            print("Invalid input. Please use HH:MM format.")

def set_alarm(alarm_hour, alarm_minute):
    try:
        while True:
            current_time = time.localtime(time.time())
            if current_time.tm_hour == alarm_hour and current_time.tm_min == alarm_minute:
                break
            time.sleep(1)
        print("It's time!")
        playsound("alarm_sound.mp3")
    except KeyboardInterrupt:
        print("Alarm clock stopped.")

def main():
    alarm_times = []

    while True:
        alarm_time = get_valid_alarm_time()
        if alarm_time is None:
            break

        alarm_times.append(alarm_time)
        alarm_times.sort()
        print(f"Alarm set for {alarm_time[0]:02d}:{alarm_time[1]:02d}")

    for alarm_time in alarm_times:
        set_alarm(alarm_time[0], alarm_time[1])

if __name__ == "__main__":
    main()
