array = [1, 2, 4, 3]

sum = 0


def largest_sum_subarray(array):
    max_sum = 0
    result = []
    for i in range(1, len(array)+1):
        for j in range(len(array)):
            subarray = []
            count = 0
            start = j
            sum = 0
            while count < i and i + j <= len(array):
                sum += array[start]
                subarray.append(array[start])
                count += 1
                start += 1
                if sum > max_sum:
                    max_sum = sum
                    result = []
                    result.append(subarray)

    return max_sum, result


result, result_array = largest_sum_subarray(array)
print(result, result_array)
