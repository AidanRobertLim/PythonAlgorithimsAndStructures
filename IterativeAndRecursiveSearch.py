# Aidan Lim
# Algorithim 3: Recursive Sort and Iterative Sort

from SelectInsertSort import*

def iterative_search(list, target, size):
    # check each item
    for num in range(size):
        if list[num] == target:
            return num
    return -1

def recursive_search(list, target, size):
    # no more items: break cycle
    if size == 0:
        return -1
    # check highest item
    elif list[size-1] == target:
        return size-1
    # check next highest item
    return recursive_search(list, target, size-1)

def recursive_binary_search(list, target, low, high):
    if low <= high:
        mid = (low + high)//2
        # eliminate bottom half: raise middle
        if list[mid] < target:
            return recursive_binary_search(list, target, mid+1, high)
        # eliminate top half: lower middle
        elif list[mid] > target:
            return recursive_binary_search(list, target, low, high-1)
        # check middle
        else:
            return mid
    # missing
    else:
        return -1

if __name__ == "__main__":
    try:
        print("enter a file.")
        myFile = open(str(input()))
        myList = myFile.read()
        print("8128705 here at", select_sort(myList, 8128705, len(myList)))
        print("5842193 here at", insert_sort(myList, 5842193, len(myList)))
    except:
        print("file not found")
        myList = [1, 2, 3, 4, 5, 6, 7]

    print("enter a number.")
    result1 = iterative_search(myList, int(input()), len(myList))
    if result1 != -1:
        print("here at", result1)
    else:
        print("not here")

    print("enter a number.")
    result2 = recursive_search(myList, int(input()), len(myList)-1)
    if result2 != -1:
        print("here at", result2)
    else:
        print("not here")

    print("enter a number.")
    result3 = recursive_binary_search(myList, int(input()), 0, len(myList)-1)
    if result3 != -1:
        print("here at", result3)
    else:
        print("not here")
