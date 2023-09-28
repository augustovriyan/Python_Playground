import time
from playsound import playsound

def set_alarm():
    try:
        # Get user input for the alarm time
        alarm_time = input("Enter the alarm time in HH:MM format: ")
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        
        # Validate the input
        if not (0 <= alarm_hour <= 23) or not (0 <= alarm_minute <= 59):
            print("Invalid time format. Please use HH:MM format.")
            return
        
        # Calculate the alarm time in seconds since midnight
        alarm_seconds = alarm_hour * 3600 + alarm_minute * 60
        
        while True:
            current_time = time.localtime()
            current_seconds = current_time.tm_hour * 3600 + current_time.tm_min * 60 + current_time.tm_sec
            
            if current_seconds == alarm_seconds:
                print("Wake up! It's time!")
                playsound("alarm_sound.mp3")  # Replace with the path to your alarm sound file
                break
            
            # Calculate the time until the next check
            time_until_next_check = alarm_seconds - current_seconds
            if time_until_next_check < 0:
                break  # Break if the alarm time has already passed
            time.sleep(time_until_next_check)

    except KeyboardInterrupt:
        print("Alarm clock stopped.")

if __name__ == "__main__":
    set_alarm()
