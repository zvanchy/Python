def pattern(n):
    for i in range(n, 0, -1):
        result = ""
        for j in range(i):
            result += str(j+1)
        print(result)


# pattern(5)


def pattern1(count, char):
    oddNumber = 1
    for i in range(count):
        print(" " * (count-i-1) + char * oddNumber)
        oddNumber += 2


pattern1(6, "*")


def pattern2(count, char):
    spaceCount = count
    print("Pattern 2")
    while count > 0:
        oddNumber = 1
        result = ""
        for _ in range(count-1):
            oddNumber += 2
        result = " " * (spaceCount - count) + char * oddNumber
        print(result)
        count -= 1


pattern2(6, "*")


def pattern3(count, char):
    print(f"character is {char}")
    result = ""
    for i in range(count):
        result += str((i+1) % 2)
        print(result)


pattern3(10, "*")


def pattern4(count):
    for i in range(count):
        result = ""
        for j in range(i+1):
            result += chr(ord("A") + j)
        print(result)


pattern4(5)
