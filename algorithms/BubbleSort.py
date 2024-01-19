unsortedArray = [4, 12, 1, 23, 2, 0, 5, 10]

"""
Bubble sort ...
loop 1 runs from n-1 to 0
loop 2 runs from 0 to i ---> swapping the elements from comparing 2...higher goes up
hence bubble sort... highest goes towards the end
"""


def bubble_sort(unsortedArray):
    for i in range(len(unsortedArray)-1, -1, -1):
        for j in range(0, i):
            if unsortedArray[j] > unsortedArray[j+1]:
                unsortedArray[j], unsortedArray[j +
                                                1] = unsortedArray[j+1], unsortedArray[j]
        print(unsortedArray)

    pass


if __name__ == '__main__':
    bubble_sort(unsortedArray)
