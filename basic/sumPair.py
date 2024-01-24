def checkPairForSum(array, target_sum):
    result = []
    for i in range(len(array)):
        for j in range(i):
            if array[i] + array[j] == target_sum:
                result.append([array[i], array[j]])
    if result is None:
        return {-1, -1}
    else:
        return result


array = [4, -1, 2, 2, 1, -2, 3, -4]
target_sum = 5
result = checkPairForSum(array, target_sum)
result = [result[i]
          for i in range(len(result)-1, -1, -1) if result[i] != result[i-1]]
print(result)


array = [0, 1, 2, 0, 1, 2, 2, 0]
zero = [element for element in array if element == 0]
one = [element for element in array if element == 1]
two = [element for element in array if element == 2]
print(zero + one + two)
