def reverse_array(array, result):
    if not array:
        # print(result)
        return result

    item = array.pop()
    result.append(item)
    return reverse_array(array, result)


array = [1, 2, 3, 4, 5]
result = []
finalresult = reverse_array(array, result.copy())
print(finalresult)
