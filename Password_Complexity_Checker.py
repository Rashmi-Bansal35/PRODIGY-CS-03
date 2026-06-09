import re

password = input("Enter Password: ")

feedback = []

if len(password) < 8:
    feedback.append("- Password should be at least 8 characters long")

if not re.search(r"[A-Z]", password):
    feedback.append("- Add at least one uppercase letter")

if not re.search(r"[a-z]", password):
    feedback.append("- Add at least one lowercase letter")

if not re.search(r"\d", password):
    feedback.append("- Add at least one number")

if not re.search(r"[!@#$%^&*]", password):
    feedback.append("- Add at least one special character")

if len(feedback) == 0:
    print("\nStrong Password")
else:
    print("\nPassword Needs Improvement:")
    for item in feedback:
        print(item)
