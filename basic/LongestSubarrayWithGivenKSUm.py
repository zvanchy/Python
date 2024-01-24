def longest_subarray_with_sum(arr, k):
    current_sum = 0
    start = 0
    max_length = 0
    end_index = -1

    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum > k:
            current_sum -= arr[start]
            start += 1

        if current_sum == k:
            if (end - start + 1) > max_length:
                max_length = end - start + 1
                end_index = end

    if end_index != -1:
        return arr[end_index - max_length + 1: end_index + 1]
    else:
        return "No subarray found"


# Example usage:
my_array = [6, 4, -1, 2, 2, 3, 4, 5]
target_sum = 5

result = longest_subarray_with_sum(my_array, target_sum)
print(result)
