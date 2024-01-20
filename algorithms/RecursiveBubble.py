def recursive_bubble_sort(unsortedArray, index):
    if index == 1:
        return
    for j in range(index):
        if unsortedArray[j] > unsortedArray[j+1]:
            unsortedArray[j], unsortedArray[j +
                                            1] = unsortedArray[j+1], unsortedArray[j]
    recursive_bubble_sort(unsortedArray, index-1)


unsortedArray = [4, 12, 1, 23, 2, 0, 5, 10]
recursive_bubble_sort(unsortedArray, len(unsortedArray)-1)
print(unsortedArray)
