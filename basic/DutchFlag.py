def dutch_flag(array):
    """
    3 pointers low, mid = 0 and high is end
    if mid = 0, increase low and mid by 1 and swap them
    if mid = 1, only increse pointer of mid by 1
    if mid = 2, swap high and mid and decrease high by 1


    """

    mid = 0
    low = 0
    high = len(array)-1

    while mid < high:
        if array[mid] == 0:
            array[low], array[mid] = array[mid], array[low]
            mid += 1
            low += 1
        elif array[mid] == 1:
            mid += 1
        elif array[mid] == 2:
            array[mid], array[high] = array[high], array[mid]
            high -= 1

    print(array)


dutch_flag([2, 1, 0, 2, 1, 0, 2, 1, 2])
