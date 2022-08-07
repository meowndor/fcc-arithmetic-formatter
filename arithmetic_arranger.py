import re

# regex for finding operator


def operator(x):
    if bool(re.search("\+", x)):
        return "+"
    elif bool(re.search("\-", x)):
        return "-"
    elif bool(re.search("\*|/", x)):
        print(x, "\nError: Operator must be '+' or '-'")
        exit()


def arithmetic_arranger(problems, showanswers=False):

    # check number of problems
    if len(problems) > 5:
        print("Error: Too many problems")
        print("Number of problems should have less than 5")
        exit()

    # check if there's more than 4 digits
    for i in problems:  # problems is in 'list' type

        splitted = i.split(operator(i))

        # traceback error for more than 4 digits
        if len(splitted[0].rstrip()) > 4:
            print(splitted[0].rstrip(),
                  "\nError: Numbers cannot be more than four digits")
            exit()

        elif len(splitted[1].lstrip()) > 4:
            print(splitted[1].lstrip(),
                  "\nError: Numbers cannot be more than four digits")
            exit()

    theanswer = ""
    firstline = ""
    secondline = ""
    theanswer = ""
    lines = ""
    for i in problems:
        splitted = list(map(int, i.split(operator(i))))

        if operator(i) == "+":
            result = splitted[0] + splitted[1]
        elif operator(i) == "-":
            result = splitted[0] - splitted[1]

        space = " "
        operand1 = len(str(splitted[0]))
        operand2 = len(operator(i) + space + str(splitted[1]))
        lenresult = len(str(result))

        maxlen = max([lenresult, operand1, operand2])

        if (operand2 - operand1) == 1:
            maxlen = maxlen + 1
        if maxlen == operand1:
            maxlen = maxlen + 2

        firstline += space * \
            (maxlen - operand1) + str(splitted[0]) + "    "
        secondline += operator(i) + space + space*(maxlen - 2 -
                                                   len(str(splitted[1]))) + str(splitted[1]) + "    "
        theresult = space*(maxlen-len(str(result))) + str(result)

        if showanswers == True:
            theanswer += theresult + "    "

        lines += "-"*maxlen + "    "

    arranged_problems = ""
    if showanswers == True:
        arranged_problems = f"{firstline}\n{secondline}\n{lines}\n{theanswer}"
    else:
        arranged_problems = f"{firstline}\n{secondline}\n{lines}"

    return arranged_problems
