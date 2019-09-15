def string_handler(curr_input, file):
    return 0


def print_func(curr_input, file):
    file.write("print(\"%s\")\n" % ' '.join(curr_input))
    print("print(\"%s\")" % ' '.join(curr_input))


def create_func(curr_input, file):
    varType = curr_input[0]
    varName = curr_input[1]
    varVal = curr_input[2]

    if varType == "integer":
        varVal = int(varVal)
    elif varType == "float":
        varVal = float(varVal)
    else:
        varVal = str(curr_input[2:])

    file.write("%s = %s\n" % (varName, varVal))
    print("%s = %s\n" % (varName, varVal))


def loop_func(curr_input, file):
    return 0


def condition_func(curr_input, file):
    return 0


def function_func(curr_input, file):
    return 0


def start_word(arr, file):
    for i in range(len(arr)):
        print("CURRENT WORD: %s " % arr[i])
        if arr[i] == "print":
            print_func(arr[i+1:], file)
        elif arr[i] == "create":
            create_func(arr[i+1:], file)
        elif arr[i] == "loop":
            loop_func(arr[i+1:], file)
        elif arr[i] == "condition":
            condition_func(arr[i+1:], file)
        elif arr[i] == "function":
            function_func(arr[i+1:], file)

