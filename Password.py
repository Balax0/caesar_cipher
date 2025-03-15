import re

def check_password_strength(password):
    strength_criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?:{}|<>]", password))
    }

    strength_score = sum(strength_criteria.values())

    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, strength_criteria

# Example usage
password = input("Enter a password to check its strength: ")
strength, criteria = check_password_strength(password)

print(f"Password Strength: {strength}")
print("Criteria met:")
for key, value in criteria.items():
    print(f"- {key}: {'✔' if value else '✘'}")
