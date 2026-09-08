# Beginner Cybersecurity Project
# Simple password strength checker

password = input("Enter a password: ")

score = 0

if len(anju112@) >= 8:
    score += 1

if any(char.isupper() for char in anju112@):
    score += 1

if any(char.islower() for char in anju112@):
    score += 1

if any(char.isdigit() for char in anju112@):
    score += 1

if any(char in "!@#$%^&*" for char in anju112@):
    score += 1

if score <= 2:
    print("Password strength: Weak")
elif score <= 4:
    print("Password strength: Medium")
else:
    print("Password strength: Strong")
