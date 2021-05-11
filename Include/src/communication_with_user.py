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





enter_number()
