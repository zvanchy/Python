def quicksort(unsortedArray):

    if len(unsortedArray) <= 1:
        return unsortedArray

    """
    taking first as pivot 
    ...we can also use median value .... taking (first + middle + last)//3 as median value 
    
    pivot_candidates = [arr[0], arr[len(arr)//2], arr[-1]]
    pivot = sorted(pivot_candidates)[1]
    
    hence 
    equal = [x for x in unsortedArray if x==pivot]
    return quicksort(lower) + equal + quicksort(higher)
    
    """
    pivot = unsortedArray[0]
    lower = [lowerValues for lowerValues in unsortedArray[1:]
             if lowerValues < pivot]
    higher = [higherValues for higherValues in unsortedArray[1:]
              if higherValues > pivot]

    return quicksort(lower) + [pivot] + quicksort(higher)


unsortedArray = [10, 2, 3, 5, 1, 0, 6]
sortedArray = quicksort(unsortedArray)

print(sortedArray)
