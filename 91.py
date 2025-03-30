import time
import datetime

def countdown_timer(total_seconds):
    while total_seconds:
        # Format seconds as HH:MM:SS
        time_format = str(datetime.timedelta(seconds=total_seconds))
        print(f"Time remaining: {time_format}", end='\r')
        time.sleep(1)
        total_seconds -= 1
    print("\nTime's up!")

if __name__ == '__main__':
    countdown_timer(100000)
