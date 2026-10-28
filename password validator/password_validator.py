def add_five(num):
    return num + 5


my_number = add_five(4)
print(my_number)


def has_min_length(password):
    return len(password) >= 8


def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False


def has_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False


def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def has_special(password):
    for char in password:
        if not char.isalnum() and not char.isspace():
            return True
    return False

# def no_space(password):
#     for char in password:
#         if char.isspace():
#             return False
#     return True


def is_valid_password(password):
    return (
        # no_space(password) and
        has_min_length(password)
        and has_uppercase(password)
        and has_lowercase(password)
        and has_digit(password)
        and has_special(password)
    )


# bonus
def get_failed_requirements(password):
    failed = []

    # if not no_space(password):
    #     failed.append("no_space")
    if not has_min_length(password):
        failed.append("min_length")
    if not has_uppercase(password):
        failed.append('Uppercase')
    if not has_lowercase(password):
        failed.append('Lowercase')
    if not has_digit(password):
        failed.append('Digits')
    if not has_special(password):
        failed.append('Special')

    return failed




