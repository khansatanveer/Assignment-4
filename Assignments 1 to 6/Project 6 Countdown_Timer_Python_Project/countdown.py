import time

def countdown_timer(seconds):
    print(f"\n⏳ Countdown started for {seconds} seconds!")

    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("⏰ Time's up!")

# User input
try:
    seconds = int(input("Enter time in seconds: "))
    countdown_timer(seconds)
    
except ValueError:
    print("⚠️ Please enter a valid number.")
