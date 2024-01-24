def moveToRight(array):
    zeros = []
    for i in range(len(array)-1, -1, -1):
        if array[i] == 0:
            array.remove(array[i])
            zeros.append(0)

    return array + zeros


array = [1, 0, 2, 3, 0, 4, 0, 1]

print(moveToRight(array))
