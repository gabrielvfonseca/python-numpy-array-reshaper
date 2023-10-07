#!/usr/bin/python
# Path: ./main.py
# Created: 18.10.2021
# Dev by Gabriel.

import random
import numpy as np
from time import sleep

# Import Modules
from modules.arrays import arrays
from modules.table import designTable
from modules.init import initialize, colors
from modules.generate import generateArrays


initialize()  # Start Program

size, max = 0, 0

while True:
    size = 4  # Default value
    max = 10  # Default value

    q = input((colors.OKGREEN + "\ninput:~ ") + colors.DEFAULT)

    if (q[0:3] == "set"):
        if (q[4:9] == "size="):
            size = int(q[9])
        elif (q[4:8] == "max="):
            max = int(q[8])

    else:
        if (q == "exit"):
            print((colors.HEADER + "Shutting down...\n") + colors.DEFAULT)
            sleep(2)
            break
        elif (q == "help"):
            print("\nList of available program commands:")
            head = ["Command", "Description"]
            row = [["'Enter'", "- List a new generated numpy array (shorted)"],
                   ["set",
                    "- Redefine default array values (size=4, max=10), syntax: \nSize: Maximum size of numpy index array => 'set size=x' \n Max: Maximum value generated inside array [0, max] => 'set max=y'"],
                   ["exit", "- Stop program"],
                   ["help", "- Show available commands and descriptions"]]

            print(designTable(head, row), "\n")
        else:
            # Generate Array
            print(
                f'Size of Array: {colors.BOLD + str(size) + colors.DEFAULT} \nInterval: [{colors.BOLD + ("0, " + str(max)) + colors.DEFAULT}]\n')

            listOfArrays = generateArrays(size, max)
            #print(listOfArrays[0], listOfArrays[1], listOfArrays[2], sep="\n")

            head = ["--", "Original Array"]
            row = [["1D", listOfArrays[0]],
                   ["2D", listOfArrays[1]],
                   ["3D", listOfArrays[2]]]

            print(designTable(head, row))

            head = ["--", "New Array"]
            row = [["1D", arrays(listOfArrays[0]).reorganize1D()],
                   ["2D", arrays(listOfArrays[1]).reorganize2D()],
                   ["3D", arrays(listOfArrays[2]).reorganize3D()]]

            print(designTable(head, row))