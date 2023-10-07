#!/usr/bin/python
# Path: ./modules/init.py
# Created: 19.10.2021
# Dev by Gabriel.

import sys
import pkg_resources


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def initialize():
    print(r"""
     ____              __                            ___
    /\  _`\           /\ \               __         /\_ \
    \ \ \ \_\     __  \ \ \____   _ __  /\_\      __\//\ \
     \ \ \  _   /'__`\ \ \ '__`\ /\`'__\\/\ \   /'__`\\ \ \
      \ \ \/, \/\ \ \.\_\ \ \ \ \\ \ \/  \ \ \ /\  __/ \_\ \_
       \ \____/\ \__/.\_\\ \_,__/ \ \_\   \ \_\\ \____\/\____\  
        \/___/  \/__/\/_/ \/___/   \/_/    \/_/ \/____/\/____/
    """)

    print("Dev by Gabriel.")
    print("This python program allows through a homemade computer terminal to set new values \nto default program variables and generate new original NumPy arrays as display \nthe same array organized by descending integers (int).\n")
    print("Packages instalation status: \n")

    i, dot = 0, ""

    # Get librarys from txt
    packages = open('requirements.txt')
    line = packages.read().replace("\n", " ")
    packages.close()
    line = line.split(" ")
    required = set(line)
    installed = {pkg.key for pkg in pkg_resources.working_set}

    missing = required - installed
    ready = required - missing

    for item in ready:
        for i in range(34 - len(item)):
            dot = '{}{}'.format(dot, ".")
            i = + 1
        print(
            f'{item} {dot} [{colors.OKGREEN}True{colors.DEFAULT}]')
        dot = ""

    for item in missing:
        for i in range(34 - len(item)):
            dot = '{}{}'.format(dot, ".")
            i = + 1
        print(
            f'{item} {dot} [{colors.FAIL}False{colors.DEFAULT}]')
        dot = ""

    print("\n")
