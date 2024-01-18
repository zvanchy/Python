userarray = [7, 3, 13, 5, 1, 6, 2, 4, 9, 8]


def selection_sort(userarray):

    for i in range(len(userarray)):
        # find minimum
        
        lowest = i
        
        for j in range(i+1, len(userarray)):
            if userarray[j] < userarray[lowest]:
                lowest = j
                
        userarray[i], userarray[lowest] = userarray[lowest], userarray[i]
        print(userarray)


selection_sort(userarray)
