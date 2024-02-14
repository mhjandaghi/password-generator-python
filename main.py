import string
import random
from os import system

settings = {
    'lower': True,
    'upper': True,
    'symbols': True,
    'numbers': True,
    'space': False,
    'length': 8
}

PW_MAX_LENGTH = 20
PW_MIN_LENGTH = 5


def clear_screen():
    system("cls")


def get_the_option_settings(option, default):
    while True:
        user_input = input(f"include {option}? "
                           f"(defualt is {default})"
                           f" (y: yes, n: no): ")

        if user_input in ["y", "n"]:
            return user_input == "y"
        
        elif user_input == "":
            return default
        
        print("invalid input!")


def get_len_password(default, pw_min = PW_MIN_LENGTH, pw_max = PW_MAX_LENGTH):
    while True:
        user_len = (input(f"enter your len pass (defualt is {default}): "))

        if user_len.isdigit():
            if  pw_min < int(user_len) < pw_max:
                return int(user_len)
            print("length of password shuold "
                  f"beetwen {pw_min} and {pw_max}!")
        
        elif user_len == "":
            return default
        else:
            print("not correct!")
        print("Try again!")


def get_settings_from_user(settings):

    for option , default in settings.items():
        if option != "length":
            settings[option] = get_the_option_settings(option, default)
        else:
            settings["length"] = get_len_password(default)         


def get_random_upper_case():
    return random.choice(string.ascii_uppercase)


def get_random_lower_case():
    return random.choice(string.ascii_lowercase)

def get_random_symbol():
    return random.choice("!@#$%^&*()_+=-~`|:")


def generate_char(choices):
    cate_choice = random.choice(choices)

    if cate_choice == "upper":
        return get_random_upper_case()
    if cate_choice == "lower":
        return get_random_lower_case()
    if cate_choice == "symbols":
        return  get_random_symbol()
    if cate_choice == "numbers":
        return random.choice("0123456789")
    if cate_choice == "space":
        return " "
    


def password_generator(settings):
    final_password = ""
    pass_length = settings["length"]

    choices = list(filter(lambda key: settings[key] == True, settings.keys()))

    for _ in range(pass_length):
        final_password += generate_char(choices)

    return final_password



def check_input_password():
    while True:
        user_pass = input("do you want another passwprd?: ")
        if user_pass.lower() in ["y","n", ""]:
            if user_pass == "n":
                return False
            return True     
        else:
            print("invalid input!")



def password_loop_print(settings):
    while True:
        print("-" * 15)
        print(f"the password: {password_generator(settings)}")
        if check_input_password() == False:
            break


def enable_default_settings():
    while True:
        user_choice = input("do you want change settings?: ")

        if user_choice.lower() in ["y", "n", ""]:
            if user_choice in ["y", ""]:
                print("-" * 6, " Chaning ", "-" * 6, sep="")
                get_settings_from_user(settings)
            break
        else:
            print("invalid-input!")


def run():
    clear_screen()
    enable_default_settings()
    password_loop_print(settings)
    print("-" * 12)
    print("Thank you for chosing us!")
   
run()
# with open("my_pass.txt", "w") as file:
#     clear_screen()
#     enable_default_settings()
#     gen = password_generator(settings)
#     file.write(gen)
#     print(f"The password is: {gen}")
#     if check_input_password() == False:
#         file.close()
    