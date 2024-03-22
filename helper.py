from argparse import ArgumentTypeError
from os import path, popen
from time import sleep


# function: check if the input is a valid color type it must be a number between 2 and 256
def colorType(arg):
    if not 2 <= int(arg) <= 70:
        raise ArgumentTypeError("Color must be a number between 2 and 256")
    return arg

def ValidateFile(file):
    if not path.exists(file):
        raise ArgumentTypeError("File does not exist")
    return file


def resizeTheTerminal(wanted_width, wanted_height):
    print(r"Resizing the terminal to fit the image")
    print(f"wanted width: {wanted_width} wanted height: {wanted_height}\n\n\n\n\n\n")

    i = 0
    while True:
        sleep(0.5)
        i += 1

        rows, columns = getTerminalSize()
        print(f"Rows: {rows} Columns: {columns}", end="\r")

        if i == 10:
            agree = input("Rows: {rows} Columns: {columns}\nDo you want to resize the image to fit the terminal? [y/n]: ")
            if agree == "y":
                resize = True
                break


        if columns >= wanted_width:
            break
        break
    
    return columns, rows 

def getTerminalSize():
    rows, columns = popen('stty size', 'r').read().split()
    return  int(columns),int(rows)
  