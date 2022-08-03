import re

#regex for finding operator
def operator(x):
    if bool(re.search("\+", x)):
        return "+";
    elif bool(re.search("\-", x)):
        return "-"



def arithmetic_arranger(problems, showanswers=False):

    #check if number of problems 
    if len(problems) > 5:
        print("Error: Too many problems")
        print("Number of problems should have less than 5")
        exit()



    #check if there's more than 4 digits
    for i in problems: #problems is in 'list' type
        splitted = i.split(operator(i))
        
        #traceback error for more than 4 digits
        if len(splitted[0]) > 4:
            print(splitted[0],"\nError: Numbers cannot be more than four digits")
            exit()

        elif len(splitted[1]) > 4:
            print(splitted[1], "\nError: Numbers cannot be more than four digits")
            exit()




     #turn every splitted items into integer then make it list in pair
    for i in problems: #problems is in 'list' type
        splitted = i.split(operator(i))

        a = list(map(int, splitted))
        print(a)

arithmetic_arranger(["1334+3222","8287-234","2334+56","234+23"])