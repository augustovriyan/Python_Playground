import time
import threading

def stopwatch():
    def print_elapsed_time():
        while not stop_event.is_set():
            elapsed_time = time.time() - start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            milliseconds = int((elapsed_time % 1) * 1000)
            print(f"\rElapsed time: {minutes:02d}:{seconds:02d}.{milliseconds:03d}", end='', flush=True)
            time.sleep(0.01)  # Adjust the sleep duration as needed

    input("Press Enter to start the stopwatch...")
    print("Stopwatch started.")
    stop_event = threading.Event()

    start_time = time.time()
    timer_thread = threading.Thread(target=print_elapsed_time)
    timer_thread.start()

    input("\n\nPress Enter to stop the stopwatch...")
    stop_event.set()

    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time % 1) * 1000)

    print(f"\nElapsed time: {minutes:02d}:{seconds:02d}.{milliseconds:03d}")

stopwatch()
