from prompt_toolkit import prompt
import re

def arithmetic_arranger(problems, showanswers=False):
    if len(problems) > 5:
        print("Error: Too many problems")
        exit()

    #split
    for i in problems:
        splitted = i.split("+")

        for a in splitted:

            b = int(a)
            #tracaback error for more than 4 digits
            if len(str(b)) > 4:
                print(b,"\nError: Numbers cannot be more than four digits")
                exit()
            #turn into integer
            


            print(b)

arithmetic_arranger(["1334+34","8234+234","234+56","234+23"])