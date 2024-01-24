def removeDuplicates(sortedArray):
    # new_sorted = []
    for i in range(len(sortedArray)-1, 0, -1):
        if sortedArray[i] == sortedArray[i-1]:
            sortedArray.remove(sortedArray[i])
    return sortedArray


sortedArray = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5]
print(removeDuplicates(sortedArray))
