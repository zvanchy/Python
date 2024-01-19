
def insertion_sort(unsortedArray):
    for i in range(1, len(unsortedArray)):
        j = i
        while j > 0 and unsortedArray[j] < unsortedArray[j-1]:
            unsortedArray[j], unsortedArray[j-1] = unsortedArray[j-1], unsortedArray[j]
            j -= 1
        print(unsortedArray)
                


unsortedArray = [4, 12, 1, 23, 2, 0, 5, 10]
insertion_sort(unsortedArray)