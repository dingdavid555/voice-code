class OpenFile:
    def __init__(self):
        self.open_variables = {}
        self.tabs = 0


def string_handler(curr_input, file):
    return 0


def print_func(curr_input, file, curr_file):
    file.write("print(\"%s\")\n" % ' '.join(curr_input))

    if ' '.join(curr_input) in curr_file.open_variables:
        print("print(%s)", ' '.join(curr_input))
    else:
        print("print(\"%s\")" % ' '.join(curr_input))


def comment_func(curr_input, file):
    output = ' '.join(curr_input)
    file.write('#' + output + '\n')
    print('#' + output + '\n')

def create_func(curr_input, file, curr_file):
    varType = curr_input[0]
    varName = curr_input[1]
    varVal = curr_input[2]

    if varType == "integer":
        varVal = int(varVal)
    elif varType == "float":
        varVal = float(varVal)
    else:
        varVal = str(' '.join(curr_input[2:]))

    curr_file.open_variables[varName] = varVal

    file.write("%s = %s\n" % (varName, varVal))
    print("%s = %s\n" % (varName, varVal))


def loop_func(curr_input, file, curr_file):
    file.write('for ' + curr_input[0] + ' in range ' + curr_input[1] + ':' + '\n')


def condition_func(curr_input, file, curr_file):
    return 0


def function_func(curr_input, file, curr_file):
    return 0


def start_word(arr, file, curr_file):
    for i in range(len(arr)):
        print("CURRENT WORD: %s " % arr[i])
        for i in range (curr_file.tabs):
            file.write('\t')   
        if (arr[i] == "print") or (arr[i] == "prince"):
            print_func(arr[i+1:], file, curr_file)
        elif arr[i] == "create":
            create_func(arr[i+1:], file, curr_file)
        elif arr[i] == "loop":
            loop_func(arr[i+1:], file, curr_file)
            curr_file.tabs += 1
        elif arr[i] == "finish":
            if curr_file.tabs == 0:
                print('Nothing to finish here...')
            else: 
                curr_file.tabs -= 1;
        elif arr[i] == "condition":
            condition_func(arr[i+1:], file, curr_file)
        elif arr[i] == "function":
            function_func(arr[i+1:], file, curr_file)
        elif (arr[i] == "comment") or (arr[i] == "comments"):
            comment_func(arr[i+1:], file, curr_file)

