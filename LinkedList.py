# Aidan Lim
# Data Structure 1: Linked Lists

import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert(head, mode, value):
    # creates node
    newNode = Node(value)
    newNode.next = head

    if head != None and (mode == "start" or mode == "end"):
        # moves current to end node
        current = head
        while (current.next != head):
            current = current.next
        # places node after end node
        current.next = newNode
    elif head != None:
        # moves current a random amount of times
        current = head
        for i in range(random.randint(0,10)):
            current = current.next
        # places data before random node
        newNode.next = current.next
        current.next = newNode
    # creates only node, and creates circular loop
    else:
        newNode.next = newNode

    # current is now the new head
    if mode == "start":
        head = newNode 
    return head

def delete(head, mode):
    # nothing to delete
    if head == None:
        return
    # delete only node
    elif head.next == head:
        head = None
        return
    # delete head node
    current = head
    if mode == "start":
        while current.next != head:
            current = current.next
        # skips over head node and creates new head node
        current.next = head.next
        head = current.next
    # delete end node
    elif mode == "end":
        while current.next.next != head:
            current = current.next
        # skips over end node
        current.next = head
    # delete random node
    else:
        for i in range(random.randint(0,10)):
            current = current.next
        # skips over random node
        randomNode = current.next
        current.next = current.next.next
    return head

def search(head, target):
    current = head
    # check each node until loops back to head
    while current.next != head:
        if current.data == target:
            return True
        current = current.next
    return False

def sort(head):
    # nothing to sort
    current = head
    # consider each data
    while current.next != head:
        min = current
        other = current.next
        # compare data with every other data
        while other.next != head:
            # replace minimum
            if other.data > min.data:
                min = other
            other = other.next
        # swap nodes
        minNot = current.data
        current.data = min.data
        min.data = minNot
        current = current.next   

def read(head):
    if head != None:
        current = head
        # print current until right before the head
        while (current.next != head):
            print(current.data, end = ' ')
            current = current.next
        print(current.data)
    # empty list
    else:
        print("empty")
    print()
    

if __name__ == "__main__":
    myHead = None
    myHead = insert(myHead, "start", 1)
    myHead = insert(myHead, "start", 9)
    myHead = insert(myHead, "start", 2)
    myHead = insert(myHead, "start", 8)
    myHead = insert(myHead, "start", 3)
    myHead = insert(myHead, "start", 7)
    myHead = insert(myHead, "start", 4)
    print("Interact with list?")
    response = input()
    while response == "yes":
        print("Chose action.")
        action = input()
        if action == "add":
            print ("Enter mode and number")
            myHead = insert(myHead, str(input()), int(input()))
        elif action == "remove":
            print("Enter mode")
            myHead = delete(myHead, str(input()))
        elif action == "search":
            print("Enter number")
            print(search(myHead, int(input())))
        elif action == "sort":
            sort(myHead)
        elif action == "print":
            read(myHead)
        else:
            print("Invalid input.")
        print("Continue?")
        response = input()