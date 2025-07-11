import random

def play_game():
    number = random.randint(1, 10)
    guess = int(input("Guess a number (1-10): "))
    if guess == number:
        print("🎉 Correct!")
    else:
        print(f"😢 Wrong! The number was {number}")

if __name__ == "__main__":
    play_game()
# quickdraw test: Sat Jul 12 02:37:39 MPST 2025
