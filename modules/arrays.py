#!/usr/bin/python
# Path: ./modules/arrays.py
# Created: 23.10.2021
# Dev by Gabriel.

import random
import numpy as np


class arrays:
    def __init__(self, arr):
        self.array = arr

    def reorganize1D(self):
        # Reorganize values and indexes on 1D array
        arr = self.array

        for i in range(len(arr)):
            for x in range(i + 1, len(arr)):
                if arr[i] > arr[x]:
                    arr[i], arr[x] = arr[x], arr[i]

        return (arr)  # Return Array

    def reorganize2D(self):
        # Reorganize values and indexes on 2D array
        arr = self.array

        for c in range(len(arr)):
            for b in range(len(arr[c])):
                for i in range(b + 1, len(arr[c])):
                    if arr[c][b] > arr[c][i]:
                        arr[c][b], arr[c][i] = arr[c][i], arr[c][b]

        return (arr)  # Return Array

    def reorganize3D(self):
        # Reorganize values and indexes on 3D array
        arr = self.array

        for c in range(len(arr)):
            for b in range(int(len(arr[c]))):
                for w in range(len(arr[c][b])):
                    for i in range(w + 1, len(arr[c][b])):
                        if arr[c][b][w] > arr[c][b][i]:
                            arr[c][b][w], arr[c][b][i] = arr[c][b][i], arr[c][b][w]

        return (arr)  # Return Array
