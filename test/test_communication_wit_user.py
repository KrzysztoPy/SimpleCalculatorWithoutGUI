from Include.src.communication_with_user import is_number, give_all_number


def test_is_number():
    static_samples = ['1', '-5', '192.345', '-992.36764', 'x', '-12.xx', '', ' ', 'a']
    expected_result = [True, True, True, True, False, False, False, False, False]

    for position in range(0, static_samples.__len__()):
        assert is_number(static_samples[position]) == expected_result[position]

def test_give_all_number():
    static_samples = ['1', '-5', '192.345', '-992.36764', 'x', '-12.xx', '', ' ', 'a']

