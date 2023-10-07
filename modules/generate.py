#!/usr/bin/python
# Path: ./modules/generate.py
# Created: 22.10.2021
# Dev by Gabriel.

import random
import numpy as np


def generateArrays(s, i):
    # Function to generate numeric arrays
    # size = Size of Array (n of index) | max = generate number between interval [0, max]
    d = int(s/2)

    arr1 = np.random.randint(i, size=10)
    arr2 = np.random.randint(i, size=(d, s))
    arr3 = np.random.randint(0, i, size=(d, int(i/4), s))

    arrays = [arr1, arr2, arr3]
    return (arrays)
