import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer_format = '{:02d}:{:02d}'.format(mins, secs)
        print(timer_format, end="\r", flush=True)
        time.sleep(1)
        t -= 1
    print("Time's up!           ")

# Start a 100 second countdown
countdown(100)
