def majorityElementInArray(array):
    """
    This only works if the array has element with occurrence more than n/2

    Args:
        array : input array to find the majority element

    Returns:
       element: if majority element is present
       -1 : if majority element is not present
    """
    element = None
    count = 0

    for i in range(len(array)):
        if count == 0:
            element = array[i]
            count += 1
        elif element != array[i]:
            count -= 1
        elif element == array[i]:
            count += 1

    cnt1 = 0
    n = len(array)
    for i in range(n):
        if array[i] == element:
            cnt1 += 1

    if cnt1 > (n / 2):
        return element
    return -1


array = [0, 1, 0, 1, 1, 1, 1, 2, 2, 1]
majorElement = majorityElementInArray(array)
print(majorElement)
