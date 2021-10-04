def is_number(str):
    try:
        num=int(str)
        return num
    except ValueError:
        return None


def is_valid_operator(operator):
    valid_operators= ["+","-","*","/"]
    if operator in valid_operators:
        return True
    else:
        return False


def ask_for_a_number(force_valid_input):
    while(True):
        answer = input("Please provide a number\n")
        if is_number(answer) == True:
            return answer
        else:
            input("This didn't look like a number, try again.")


def ask_for_an_operator(force_valid_input):
    pass


def calc(operator, a, b):
    pass


def simple_calculator():
    pass


if __name__ == '__main__':
    simple_calculator()
