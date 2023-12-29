#my_list = [1,2,12,2,34,32,45]
my_list = [1,2,12,2,34,32,45]

def reversed_list(args):
    return [args[i] for i in range(len(args)-1,0,-1)]


print(reversed_list(my_list))


def max_min(unsorted_list):
    min = unsorted_list[0]
    max = unsorted_list[0]
    
    for i in range(1, len(unsorted_list)):
        if max < unsorted_list[i]:
            max = unsorted_list[i]
        if min > unsorted_list[i]:
            min = unsorted_list[i]
            
            
max_min(my_list)

