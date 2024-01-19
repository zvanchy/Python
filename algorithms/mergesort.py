# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]

#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)

#     return merge(left_half, right_half)


# def merge(left, right):
#     result = []
#     left_idx = 0
#     right_idx = 0

#     while left_idx < len(left) and right_idx < len(right):
#         if left[left_idx] <= right[right_idx]:
#             result.append(left[left_idx])
#             left_idx += 1
#         else:
#             result.append(right[right_idx])
#             right_idx += 1

#     result.extend(left[left_idx:])
#     result.extend(right[right_idx:])

#     return result


# Example usage


def merge_sort(unsorted_array):
    if len(unsorted_array) <= 1:
        return unsorted_array

    middle = len(unsorted_array)//2

    left = unsorted_array[:middle]
    right = unsorted_array[middle:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    left_index = 0
    right_index = 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        elif right[right_index] < left[left_index]:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


unsorted_array = [4, 12, 1, 23, 2, 0, 5, 10]
sorted_array = merge_sort(unsorted_array)
print(sorted_array)
