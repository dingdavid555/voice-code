def print_func(curr_input):
    return 0


def create_func(curr_input):
    return 0


def loop_func(curr_input):
    return 0


def condition_func(curr_input):
    return 0


def function_func(curr_input):
    return 0


def start_word(arr):
    for i in range(len(arr)):
        if arr[i] == "print":
            print_func(arr[i:])
        elif arr[i] == "create":
            create_func(arr[i:])
        elif arr[i] == "loop":
            loop_func(arr[i:])
        elif arr[i] == "condition":
            condition_func(arr[i:])
        elif arr[i] == "function":
            function_func(arr[i:])

