def is_palindrome(text):
    return text == text[::-1]

if __name__ == "__main__":
    txt = input("Enter a word: ")
    if is_palindrome(txt):
        print("🪞 It's a palindrome!")
    else:
        print("🚫 Not a palindrome.")
