import re


def email_validation(email):
    email_regex = r"^[a-zA-Z0-9_.+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if not re.match(email_regex, email):
        return False
    return True


def password_validation(password):
    password_regex = r"^(?=.*[!@#$%^&])(?=.*[a-z])(?=.[A-Z])(?=.*\d).{7,}$"
    if not re.match(password_regex, password):
        return False
    return True
