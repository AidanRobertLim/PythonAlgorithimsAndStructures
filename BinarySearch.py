# Aidan Lim
# Algorithim 1: Binary Search

def binary_search(list, target, low, high):
    operationCount = 0
    while low <= high:
        # count operations
        operationCount = operationCount + 1
        mid = (high + low)//2
        # eliminate bottom half, raise middle
        if list[mid] < target:
            low = mid + 1
        # eliminate top half, lower middle
        elif list[mid] > target:
            high = mid - 1
        # check middle
        else:
            return operationCount
    # missing
    return -1

if __name__ == "__main__":
    try:
        print("Enter file")
        myFile = open(str(input()))
        myList = myFile.read()
        print("51216352 here after", binary_search(myList, 51216352, 0, len(myList)))
        print("198313119 here after", binary_search, 198313119, 0, len(myList))
        print("196614208 here after", binary_search, 196614208, 0, len(myList))
        # d. worst case time complexity: log[2]2000, O(log[2]n)
        # e. worst case time complexity: log[2]4000
    except:
        print("File not found")
        myList = [1, 2, 3, 4, 5, 6, 7]

    print("Enter number")
    result = binary_search(myList, int(input()), 0, len(myList))
    if result != -1:
        print("Here after", result, "operations")
    else:
        print("Not here")