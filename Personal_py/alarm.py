import time
from playsound import playsound

def set_alarm():
    # Get user input for the alarm time
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up! It's time!")
            playsound("alarm_sound.mp3")  # Replace with the path to your alarm sound file
            break
        time.sleep(60)  # Check the time every minute

if __name__ == "__main__":
    set_alarm()
