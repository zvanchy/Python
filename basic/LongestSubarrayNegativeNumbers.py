

def longest_subarray_with_sum(array, target_sum):
    for windowSize in range(1,len(array)+1):
        end = len(array)
        current_sum = 0
        result = []
        start = 0

        while start < end and start+windowSize <= end:
            if windowSize == 0:
                break
            for i in range(windowSize):
                current_sum += array[start+i]
                result.append(array[start+i])
                # start += i
            if current_sum == target_sum:
                print(result)
                current_sum = 0
                result = []
                start += 1
            else:
                current_sum = 0
                result = []
                start += 1
        pass


my_array = [6, 4, -1, 2, 2, 1, - 2, 3, -4, 5]
target_sum = 5

result = longest_subarray_with_sum(my_array, target_sum)
print(result)
