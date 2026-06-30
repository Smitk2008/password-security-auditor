import math
import re

# Load common passwords
with open("common_passwords.txt", "r") as file:
    common_passwords = [line.strip().lower() for line in file]

password = input("Enter Password: ")

# Password strength score
score = 0

if len(password) >= 8:
    score += 1

if re.search(r"[A-Z]", password):
    score += 1

if re.search(r"[a-z]", password):
    score += 1

if re.search(r"\d", password):
    score += 1

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

# Strength classification
if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

# Character set size
charset = 0

if re.search(r"[a-z]", password):
    charset += 26

if re.search(r"[A-Z]", password):
    charset += 26

if re.search(r"\d", password):
    charset += 10

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    charset += 32

# Entropy calculation
entropy = len(password) * math.log2(charset) if charset > 0 else 0

# Dictionary check
if password.lower() in common_passwords:
    dictionary_result = "Common Password Found"
else:
    dictionary_result = "Safe"

# Crack time estimate
if entropy < 40:
    crack_time = "Few Seconds"
elif entropy < 60:
    crack_time = "Few Days"
else:
    crack_time = "Many Years"

# Display results
print("\n----- PASSWORD SECURITY REPORT -----")
print("Strength:", strength)
print("Entropy:", round(entropy, 2), "bits")
print("Dictionary Check:", dictionary_result)
print("Estimated Crack Time:", crack_time)

# Save report
with open("report.txt", "w") as report:
    report.write("PASSWORD SECURITY REPORT\n")
    report.write(f"Strength: {strength}\n")
    report.write(f"Entropy: {round(entropy,2)} bits\n")
    report.write(f"Dictionary Check: {dictionary_result}\n")
    report.write(f"Estimated Crack Time: {crack_time}\n")

print("\nReport saved to report.txt")