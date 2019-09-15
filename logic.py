class OpenFile:
    def __init__(self):
        self.open_variables = {}
        self.tabs = 0


def string_handler(curr_input, file, curr):
    return 0


def print_func(curr_input, file, curr_file):
    output = ""
    for i in range(curr_file.tabs):
        output += "\t"
    output += ""

    if ' '.join(curr_input) in curr_file.open_variables:
        output += "print(%s)", ' '.join(curr_input)
    else:
        output += "print(\"%s\")" % ' '.join(curr_input)

    file.write(output)


def comment_func(curr_input, file, curr_file):
    output = ""
    for i in range(curr_file.tabs):
        output += '\t'

    output += "# " + ' '.join(curr_input)
    file.write(output)
    print(output)

def create_func(curr_input, file, curr_file):
    for i in range (curr_file.tabs):
        file.write('\t')
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

    output = ""
    for i in range(curr_file.tabs):
        output += '\t'
    output += "%s = %s\n" % (varName, varVal)

    file.write(output)
    print(output)


def loop_func(curr_input, file, curr_file):

    output = ""
    for i in range(curr_input):
        output += "\t"


    num = curr_input[1]
    if (num == 'one'):
        curr_input[1] = 1
    elif (num == 'two'):
        curr_input[1] = 2
    elif (num == 'three'):
        curr_input[1] = 3
    elif (num == 'four'):
        curr_input[1] = 4
    elif (num == 'five'):
        curr_input[1] = 5
    elif (num == 'six'):
        curr_input[1] = 6

    output += 'for ' + curr_input[0] + ' in range ' + curr_input[1] + ':' + '\n'

    file.write(output)

def condition_func(curr_input, file, curr_file):
    var1 = curr_input[0]
    oper = curr_input[1]
    var2 = curr_input[2]

    if (oper == "equals") or (oper == "equal"):
        oper = "=="

    elif ((oper == "less") and (curr_input[2] == "than")):
        var2 = curr_input[3]
        oper = "<"

    elif ((oper == "greater") and (curr_input[2] == "than")):
        var2 = curr_input[3]
        oper = ">"

    print("if " + var1 + oper + var2 + ":" + "\n")

    return 0


def function_func(curr_input, file, curr_file):
    return 0


def start_word(arr, file, curr_file):
    for i in range(len(arr)):
        print("CURRENT WORD: %s " % arr[i])
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
