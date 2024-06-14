import re

def assess_password_strength(password):
    length_weight = 1.5
    uppercase_weight = 1.0
    lowercase_weight = 1.0
    number_weight = 1.0
    special_char_weight = 1.5

    feedback = []

    length_score = len(password) * length_weight
    if len(password) < 8:
        feedback.append("Password is too short (less than 8 characters).")
    elif len(password) < 12:
        feedback.append("Password length is adequate but could be longer.")
    else:
        feedback.append("Good password length.")

    if re.search(r'[A-Z]', password):
        uppercase_score = uppercase_weight
        feedback.append("Contains uppercase letters.")
    else:
        uppercase_score = 0
        feedback.append("No uppercase letters found.")

    if re.search(r'[a-z]', password):
        lowercase_score = lowercase_weight
        feedback.append("Contains lowercase letters.")
    else:
        lowercase_score = 0
        feedback.append("No lowercase letters found.")

    if re.search(r'[0-9]', password):
        number_score = number_weight
        feedback.append("Contains numbers.")
    else:
        number_score = 0
        feedback.append("No numbers found.")

    if re.search(r'[\W_]', password):
        special_char_score = special_char_weight
        feedback.append("Contains special characters.")
    else:
        special_char_score = 0
        feedback.append("No special characters found.")

    total_score = length_score + uppercase_score + lowercase_score + number_score + special_char_score

    if total_score >= 10:
        strength = "Strong"
    elif total_score >= 7:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "strength": strength,
        "score": total_score,
        "feedback": feedback
    }

password = "Prodigy@9017"
result = assess_password_strength(password)
print(f"Password Strength: {result['strength']}")
print(f"Score: {result['score']}")
print("Feedback:")
for msg in result["feedback"]:
    print(f"- {msg}")
