import re

def arithmetic_arranger(problems, showanswers=False):
    if len(problems) > 5:
        print("Error: Too many problems")
        exit()

    #check if there's digits for more than 4
    for i in problems: #problems is 'list' type
        splitted = i.split("+")
        

        #traceback error for more than 4 digits
        if len(splitted[0]) > 4:
            print(splitted[0],"\nError: Numbers cannot be more than four digits")
            exit()

        elif len(splitted[1]) > 4:
            print(splitted[1],"\nError: Numbers cannot be more than four digits")
            exit()

    for i in problems: #problems is 'list' type
        splitted = i.split("+")

        a = list(map(int,splitted)) #turn every splitted items into integer then make it list in pair
        print(a)

arithmetic_arranger(["1334+3222","8287+234","2334+56","234+23"])