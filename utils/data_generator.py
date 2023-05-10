def generate_test_data():
    return [
        ("video1.mp4", 100),
        ("video2.mp4", 200),
        ("video3.mp4", 300),
    ]


def get_value(list_account):
    for code in list_account:
        if code[1] == 200:
            return code


print(get_value(generate_test_data()))