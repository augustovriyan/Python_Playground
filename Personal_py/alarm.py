import time
from playsound import playsound

def get_valid_alarm_time():
    while True:
        try:
            # Get user input for the alarm time
            alarm_time = input("Enter the alarm time in HH:MM format: ")
            alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
            
            # Validate the input
            if 0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59:
                return alarm_hour, alarm_minute
            else:
                print("Invalid time format. Please use HH:MM format.")

        except ValueError:
            print("Invalid input. Please use HH:MM format.")

def calculate_seconds_until_alarm(alarm_hour, alarm_minute):
    current_time = time.localtime()
    current_seconds = current_time.tm_hour * 3600 + current_time.tm_min * 60 + current_time.tm_sec
    
    alarm_seconds = alarm_hour * 3600 + alarm_minute * 60
    seconds_until_alarm = alarm_seconds - current_seconds if alarm_seconds >= current_seconds else 86400 - current_seconds + alarm_seconds

    return seconds_until_alarm

def set_alarm():
    try:
        alarm_hour, alarm_minute = get_valid_alarm_time()
        seconds_until_alarm = calculate_seconds_until_alarm(alarm_hour, alarm_minute)

        print(f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}")

        time.sleep(seconds_until_alarm)

        print("Wake up! It's time!")
        playsound("alarm_sound.mp3")  # Replace with the path to your alarm sound file

    except KeyboardInterrupt:
        print("Alarm clock stopped.")

if __name__ == "__main__":
    set_alarm()
