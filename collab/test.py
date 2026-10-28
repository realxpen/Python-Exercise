# current_year = 2026

# birth_year = int(input('Input Your Year of Birth: '))

# current_age = current_year - birth_year

# if current_age < 0:
#     result = 'Are you from the Future'
# elif current_age < 13:
#     result = 'Child'
# elif current_age < 20:
#     result = 'Teenager'
# elif current_age < 50:
#     result = 'Adult'
# else:
#     result = 'Elder'

# print(result)

# age = 15

# if age < 12:
#     presult = '$5'
# elif age <=17:
#     presult = '$10'
# else:
#     presult = '$15'
# print(presult)

# favorite_foods = ["Jollof Rice", "Amala", "Yam"]
# # favorite_foods.append('Pasta')
# favorite_foods[2] = "Plantain"
# # first_food = favorite_foods[0]
# # last_food = favorite_foods[-1]
# # print(first_food)
# # print(last_food)
# # print(favorite_foods)
# for food in favorite_foods:
#     result = f"I love eating {food}"
#     print(result)


# person = {"name": "Ayomide", "age": 18}

# person["country"] = "Nigeria"
# result = (
#     f"{person['name']} is {person['age']} years old and lives in {person['country']}."
# )
# print(result)

# for key, value in person.items():
#     result = f"{key} -> {value}"
#     print(result)


# def welcome_user(username):
#     result = f"Welcome back to Python, {username}!"
#     print(result)


# welcome_user("Ayomide")
# welcome_user("Xpen")


def add_five(num):
    return num + 5


my_number = add_five(4)
print(my_number)

def has_min_length(password):
    if len(password) >= 8:
        return True
    return False


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
        if not char.isalnum():
            return True
    return False


def is_valid_password(password):
    if has_min_length(password) and
    has_uppercase(password) and
    has_lowercase(password) and
    has_digit(password) and 
    has_special(password):
        return True
    return False
    
    


# bonus
def get_failed_requirements(password):
    # Write your code here
    pass
