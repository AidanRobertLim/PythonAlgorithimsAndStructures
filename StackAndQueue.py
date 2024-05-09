# Aidan Lim
# Data Structure 2: Stacks and Queues

# node functions
from Structure1 import*

# stack functions
def emptyStack(stack):
    return len(stack) == 0

def fullStack(stack):
    return len(stack) != 0

def readStack(stack):
    print("Stack:")
    for i in range(len(stack)):
        print(stack[i], end=' ')
    print()
        
# queue functions
class Queue:
    def __init__(self):
        front = rear = None

def emptyQueue(head):
    return head == None

def fullQueue(head):
    return head != None
    
def enQueue(head, value):
    newNode = Node(value)
    # base case
    if head.front == None:
        head.front = newNode
    # initiate queue: move behind rear
    else:
        head.rear.next = newNode
    # initiate circular: connect rear to front
    head.rear = newNode
    head.rear.next = head.front

def deQueue(head):
    # zero case
    if head.front == None:
        print("Empty.")
    # base case
    if head.front == head.rear:
        value = head.front.data
        head.front = head.rear = None
    else:
        target = head.front
        value = target.data
        # skip over front
        head.front = head.front.next
        head.rear.next = head.front

if __name__ == "__main__":
    myStack = [1, 2, 3]
    myHead = Queue()
    myHead.front = myHead.rear = None
    enQueue(myHead, 1)
    enQueue(myHead, 2)
    enQueue(myHead, 3)

    print("Interact with stack?")
    response = input()
    while response == "yes":
        print("Chose action.")
        action = input()
        if action == "add":
            myStack.append(input())
        elif action == "remove":
            myStack.pop()
        elif action == "empty":
            print(emptyStack(myStack))
        elif action == "full":
            print(fullStack(myStack))
        elif action == "peek":
            print(myStack[len(myStack)])
        elif action == "print":
            readStack(myStack)
        else:
            print("Invalid Input.")
        print("Continue?")
        response = input()

    print ("Interact with Queue?")
    response = input()
    while response == "yes":
        print("Chose action.")
        action = input()
        if action == "add":
            enQueue(myHead, input())
        elif action == "remove":
            deQueue(myHead)
        elif action == "empty":
            print(emptyQueue(myHead))
        elif action == "full":
            print(fullQueue(myHead))
        elif action == "peek":
            print(myHead.front.data)
        elif action == "print":
            read(myHead.front)
        else:
            print("Invalid input")
        print("Continue?")
        response = input()
