import communication_with_user_GUI as comm_gui
import os


def enter_number():
    print(comm_gui.information_about_quantity_enter_number_gui())
    print(comm_gui.quantity_enter_number_gui())

    user_answer = input()

    if user_answer.isnumeric() and int(user_answer) != 0:
        comm_gui.clear_console()
        give_all_number(user_answer)
    else:
        print(comm_gui.error_number_not_is_integer_gui() + '\n')
        enter_number()


def is_number(input_data):
    try:
        float(input_data)
        return True
    except ValueError:
        return False


def give_all_number(user_answer):
    lists_with_value_numbers = list()
    user_answer = int(user_answer)

    for number in range(0, user_answer):
        while True:
            print(comm_gui.enter_value_of_the_number_gui(number))
            input_data = input()
            if is_number(input_data):
                lists_with_value_numbers.append(input_data)
                break
            else:
                comm_gui.clear_console()
                print(comm_gui.not_integer_or_float_number_gui())

    what_action_to_perform_on_the_number(lists_with_value_numbers)


def create_mathematical_operation(lists_with_value_numbers):
    return 0


def what_action_to_perform_on_the_number(lists_with_value_numbers):
    lists_with_value_numbers = lists_with_value_numbers
    mathematical_operation = create_mathematical_operation(lists_with_value_numbers)
    available_action = ['+', '-', '*', '/', '^', '//', '%', '--']
    sequence_of_action = ['--', '%', '//', '^', '*', '/', '+', '-']

    # 1 x 1
    pass


# Notatka

