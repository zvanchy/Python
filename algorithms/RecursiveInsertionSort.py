
def insertion_sort(unsorted_array, length):

    if length < 0:
        print(unsorted_array)
        return
    for j in range(length):
        if unsorted_array[j] > unsorted_array[j+1]:
            unsorted_array[j], unsorted_array[j +
                                              1] = unsorted_array[j+1], unsorted_array[j]

    return insertion_sort(unsorted_array, length-1)


unsorted_array = [10, 2, 12, 3, 6, 1]
insertion_sort(unsorted_array, len(unsorted_array)-1)
