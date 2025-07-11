# Patch 2: Testing PR

def is_strong(password):
    return len(password) >= 8 and any(c.isdigit() for c in password)

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    if is_strong(pwd):
        print("✅ Strong password!")
    else:
        print("❌ Weak password.")
