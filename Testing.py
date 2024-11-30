from parser import parse_config

def Test_mas():
    test_text_1 = {
    'colors': ['red', 'green', 'blue', 'yellow'],
    'numbers': [3242, 4242.32, 32.311],
    'teams': [
        {'name': 'Team A', 'members': ['Alice', 'Bob']},
        {'name': 'Team B', 'members': ['Charlie', 'Dima']}
    ],
    }
    result = parse_config(test_text_1)
    assert result == (
        "array(red, green, blue, yellow)\n"
        "array(3242, 4242.32, 32.311)\n"
        "array({'name': 'Team A', 'members': ['Alice', 'Bob']}, {'name': 'Team B', 'members': ['Charlie', 'Dima']})"
    )

def Test_dictionary():
    test_text_2 = {
        'host': 7645,
        'person': {
            'name': 'John Doe',
            'age': 30,
            'is_employee': True,
            'hobbies': ['reading', 'swimming'],
            'address': {
                'street': '123 Main St',
                'city': 'Anytown'
            }
        }
    }
    result = parse_config(test_text_2)
    assert result == (
        "$[\n"
        "name is John Doe\n"
        "age is 30\n"
        "is_employee is True\n"
        "array(reading, swimming)\n"
        "$[\n"
        "street is 123 Main St\n"
        "city is Anytown\n"
        "]\n"
        "]"
    )

def Test_const():
    test_text_3 = {
        'const': {
            'f': 5,
            'h': '!{f+5}'
        }
    }
    result = parse_config(test_text_3)
    assert result == (
        "$[\n"
        "f is 5\n"
        "h is {10}\n"
        "]"
    )

def Test_calculations():
    test_text_4 = {
        'constants':{
            'a': 3,
            'b': 4,
            'c': 1.123,
            'd': 2.12
        },
        'calculations':{
            'sum':{
                'a + b': "!{a+b}"
            },
            'sub':{
                'a - b': "!{a-b}"
            },
            'mul': {
                'a * b': "!{a*b}"
            },
            'div': {
                'a / b': "!{a/b}"
            },
            'paralel': {
                '(a + b) * (a - b)': "!{(a+b)*(a-b)}"
            }
        }
    }
    result = parse_config(test_text_4)
    assert result == (
        "$[\n"
        "a is 3\n"
        "b is 4\n"
        "c is 1.123\n"
        "d is 2.12\n"
        "]\n"
        "$[\n"
        "$[\n"
        "a + b is {7}\n"
        "]\n"
        "$[\n"
        "a - b is {-1}\n"
        "]\n"
        "$[\n"
        "a * b is {12}\n"
        "]\n"
        "$[\n"
        "a / b is {0.75}\n"
        "]\n"
        "$[\n"
        "(a + b) * (a - b) is {-7}\n"
        "]\n"
        "]"
    )

def Test_len():
    test_text_5 = {
        'num':{
            - 1
            - 2
            - 3
            - 4
        },
        'len_plus_one': "!{len(num)}"
    }
    result = parse_config(test_text_5)
    assert result == (
        "len_plus_one is {1}"
    )

Test_mas()
Test_dictionary()
Test_const()
Test_calculations()
Test_len()
print("Все тесты пройдены!")