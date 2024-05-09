# Aidan Lim
# Algorithim 2: Select Sort and Insert Sort

def select_sort(list, size):
    # unsortable
    if size <= 1:
        return
    # assume min
    for i in range(size):
        min = i
        # check other items
        for n in range(i + 1, size):
            # define new min?
            if list[n] < list[min]:
                min = n
        # where min is ahead, min is behind
        (list[i], list[min]) = (list[min], list[i])

def insert_sort(list, size):
    # unsortable
    if size <= 1:
        return
    # assume mid
    for i in range(1, size):
        key = list[i]
        n = i-1
        # check other items
        while n >= 0 and key < list[n]:
            # split evenly
            list[n+1] = list[n]
            n -= 1
        # insert mid
        list[n+1] = key

if __name__ == "__main__":
    try:
        print("Enter file.")
        myFile = open(str(input()))
        myList = myFile.read()
    except: 
        print("File not found")
        myList = [5, 1, 4, 2, 3, 3]

        select_sort(myList, len(myList))
        print("Selection Sort:", myList)

        insert_sort(myList, len(myList))
        print("Insertion Sort:", myList)