# Functions with Outputs
'''
def my_function():
    return 3 * 2

output = my_function
'''

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "No valid inputs."
    formated_f = f_name.title()
    formated_l = l_name.title()
    return f"{formated_f} {formated_l}"

print(format_name(input("What is your frst name? "), input("What is your last name? ")))

