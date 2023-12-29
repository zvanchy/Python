import time

# root of 81 is 9 ...so max will be multiple of 9..
"""
hence square root of the number is the max

"""
num = int(input("Enter the number where the prime numbers are displayed: "))
start_time = time.time()

for i in range(2,num):
    for j in range(2, int(i ** 0.5) + 1):
        if(i%j == 0):
            print(f'{i} = {i} * {j}')
            break
    else:
        print(f'{i} is a prime number')

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")        