import time
import threading

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.stop_event = threading.Event()
        self.timer_thread = None

    def _print_elapsed_time(self):
        while not self.stop_event.is_set():
            elapsed_time = time.time() - self.start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            milliseconds = int((elapsed_time % 1) * 1000)
            print(f"\rElapsed time: {minutes:02d}:{seconds:02d}.{milliseconds:03d}", end='', flush=True)
            time.sleep(0.01)  # Adjust the sleep duration as needed

    def start(self):
        input("Press Enter to start the stopwatch...")
        print("Stopwatch started.")
        self.start_time = time.time()
        self.timer_thread = threading.Thread(target=self._print_elapsed_time)
        self.timer_thread.start()

    def stop(self):
        input("\n\nPress Enter to stop the stopwatch...")
        self.stop_event.set()
        self.timer_thread.join()

        end_time = time.time()
        elapsed_time = end_time - self.start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time % 1) * 1000)

        print(f"\nElapsed time: {minutes:02d}:{seconds:02d}.{milliseconds:03d}")

def main():
    stopwatch = Stopwatch()
    stopwatch.start()
    stopwatch.stop()

if __name__ == "__main__":
    main()
