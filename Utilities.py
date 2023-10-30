def build_question(s: str):
    return f"How many {s} would you like in your password?\n"


def get_int_input(s: str):
    # TODO: let user retry when wrong value is entered
    user_number = input(s)
    while not user_number.isnumeric():
        print("Please enter a number")
        user_number = input(s)

    return int(user_number)


