import os


def quantity_enter_number_gui():
    return 'How many number will you enter: '


def information_about_quantity_enter_number_gui():
    return 'You can choice only integer number from 1 to infinity.'


def error_number_not_is_integer_gui():
    return 'Please try again:'


def enter_value_of_the_number_gui(number):
    return 'Set the value of the number ' + ' {0}:'.format(number)


def not_integer_or_float_number_gui():
    return 'The given value is neither an integer or float type. Please try again.'


def clear_console():
    return os.system('cls')
