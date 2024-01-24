

def left_rotate(array, position):

    new_arr = array[position-1:]
    reversed_array = array[:position]
    
    return new_arr + reversed_array
    pass


array = [1, 2, 3, 4, 5]
array_rotated = left_rotate(array, 2)
print(array_rotated)
