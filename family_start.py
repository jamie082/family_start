#!/usr/bin/python3

from sys import exit
from sys import argv

filename = "one.txt"
txt = open(filename)

def susan_function():
    print("Susan function")

    count = 0

    while (count < 1):
        prompt = input ("susan> ")

        if prompt == "1" or prompt == "2":
            print("You entered 1 or 2")

        elif prompt == "3":
            print("You entered 3")
            break

        elif prompt == "quit":
            exit(0)

        elif prompt == "15":
            print(txt.read())

        else:
            string = 'You entered %s' % (prompt)
            print(string)

def jamie_function():
    print("Jamie function")

def dead(why):
    print(why, "Try Again!")
    exit(0)

def start():
    print("Program start...\nMenu driven program...\nv.002")
    print("Which family member?")
    print("susan")
    print("jamie")
    print("lindsey")
    
    choice = input("> ")

    if choice == "susan":
        susan_function()
    elif choice == "jamie":
        jamie_function()
    else:
        dead("Error! No Match!.")

start()
