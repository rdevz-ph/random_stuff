# Patch 1: Added this comment to test pull requests

def is_even(number):
    return number % 2 == 0

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_even(num):
        print("✅ It's even!")
    else:
        print("🔢 It's odd!")
