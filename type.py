# function to check data type of user input

def type_check(user_input):
    if type(user_input) == int:
        return "int"
    elif type(user_input) == float:
        return "float"
    elif type(user_input) == str:
        return "string"
    else:
        return "unknown"

print(type_check(input("Enter a number, float or a string: ")))