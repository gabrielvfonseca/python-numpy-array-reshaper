# array.py =========================================

def allArrayCombined(self):
    # Reorganize values and indexes
    arr = self.array

     for c in range(len(arr)):
          for b in range(len(arr[c])):

               if (type(arr[c][b]) is np.ndarray):
                    print(type(arr[c][b]))
                    # que tipo de array és
                    if (int(arr[c][b].ndim) == 2):
                        arr[c][b] = arrays(arr[c][b]).reorganize2D()
                    elif (int(arr[c][b].ndim) == 3):
                        arr[c][b] = arrays(arr[c][b]).reorganize3D()
                print(arr)


# newArray = arrays(np.array([np.array([50, 1, 20, 3]), np.array([20, 3, 0])], dtype=object)).allArrayCombined()
# print(newArray)


# generate.py ======================================

class generateMultipleArrays():
    def __init__(self, size, max):
        self.size = size
        self.max = max

    def gen1D_array(self):
        # Generate 1D array
        random_Array1 = np.array([])
        size = int(self.size)
        max = int(self.max)

        for i in range(0, size):
            numb = random.randint(1, max)
            random_Array1 = numb
        return (random_Array1)

    def gen2D_array(self):
        # Generate 1D array
        random_Array2 = np.array([])
        size = int(self.size)
        max = int(self.max)

        for x in range(0, size):
            ele2d = np.array([])
            for y in range(random.randint(1, max)):
                numb = random.randint(1, max)
                ele2d[y] = numb
            random_Array2 = ele2d
        return (random_Array2)

    def gen3D_array(self):
        # Generate 1D array
        random_Array3 = np.array([])
        size = int(self.size)
        max = int(self.max)

        for w in range(0, size):
            ele1_3d = np.array([])
            for p in range(random.randint(1, max)):
                ele2_3d = np.array([])
                for u in range(random.randint(1, max)):
                    numb = random.randint(1, max)
                    ele2_3d[u] = numb
                ele1_3d[p] = ele2_3d
            random_Array3 = ele1_3d
        return (random_Array3)


print(generateMultipleArrays(8, 8).gen2D_array())


class generateUnicArray:
    def __init__(self, size, max):
        self.size = size
        self.max = max

    def generateArray(self):
        # Generate random Array (1, 2 & 3D)
        random_Array = np.array([])
        size = int(self.size)
        max = int(self.max)

        for r in range(0, size):
            order = random.randint(1, 3)

            if (order == 1):
                random_Array = + \
                    generateMultipleArrays(size, max).gen1D_array()
            elif (order == 2):
                random_Array = + \
                    generateMultipleArrays(size, max).gen2D_array()
            else:
                random_Array = + \
                    generateMultipleArrays(size, max).gen3D_array()

        return (random_Array)


print(generateUnicArray(8, 8).generateArray())


    random_Array1, random_Array2, random_Array3 = np.array(
        [], dtype='int16'), np.array([], dtype='int16'), np.array([], dtype='int16')

    # Generate 1D array
    for i in range(0, size):
        numb = random.randint(0, max)
        random_Array1 = np.append(random_Array1, [numb])

    # Generate 2D array
    for x in range(0, size):
        ele2d = np.array([], dtype='int16')

        for y in range(random.randint(0, max)):
            numb = random.randint(1, max)
            ele2d = np.append(ele2d, [numb])
        random_Array2 = np.append(random_Array2, [ele2d])

    # Generate 3D array
    for w in range(0, size):
        ele1_3d = np.array([], dtype='int16')

        for p in range(random.randint(0, max)):
            ele2_3d = np.array([], dtype='int16')

            for u in range(random.randint(1, max)):
                numb = random.randint(0, max)
                ele2_3d = np.append(ele2_3d, [numb])

            ele1_3d = np.append(ele1_3d, [ele2_3d])
        random_Array3 = np.append(random_Array3, [ele1_3d])

    return (random_Array1,
            random_Array2, random_Array3)
