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
    arranged_problems = ""

    # check number of problems
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems
        # print("Number of problems should have less than 5")
        # exit()

    # check if there's more than 4 digits
    for i in problems:  # problems is in 'list' type

        # ---[TODO]----
        if not bool(re.search("\+|-", i.split()[1])) == True:
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems

        splitted = i.split(operator(i))

        # traceback error for more than 4 digits
        if len(splitted[0].rstrip()) > 4:
            arranged_problems = f"Error: Numbers cannot be more than four digits."
            return arranged_problems

        elif len(splitted[1].lstrip()) > 4:
            arranged_problems = f"Error: Numbers cannot be more than four digits."
            return arranged_problems

        if bool(re.search("[a-z]", splitted[0].rstrip())) or bool(re.search("[a-z]", splitted[1].rstrip())) == True:
            arranged_problems = f"Error: Numbers must only contain digits."
            return arranged_problems

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

    if showanswers == True:
        arranged_problems = f"{firstline.rstrip()}\n{secondline.rstrip()}\n{lines.rstrip()}\n{theanswer.rstrip()}"
    else:
        arranged_problems = f"{firstline.rstrip()}\n{secondline.rstrip()}\n{lines.rstrip()}"

    return arranged_problems


# print(arithmetic_arranger(['44 + 815', '909 + 2']))
