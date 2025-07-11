# Patch 3: Testing PR

import time

def countdown(seconds):
    while seconds > 0:
        print(f"⏳ {seconds} seconds remaining...")
        time.sleep(1)
        seconds -= 1
    print("⏰ Time's up!")

if __name__ == "__main__":
    countdown(5)
# quickdraw test: Sat Jul 12 02:29:51 MPST 2025
