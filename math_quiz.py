# Quickdraw test

import random

def generate_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    question = f"{a} + {b} ="
    answer = a + b
    return question, answer

if __name__ == "__main__":
    question, answer = generate_question()
    print(question)
    user_input = input("Your answer: ")
    if user_input.isdigit() and int(user_input) == answer:
        print("✅ Correct!")
    else:
        print(f"❌ Wrong! The correct answer is {answer}")
