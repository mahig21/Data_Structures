print("Implementation of Linear Queue using a list")
n=0
queue=[]

def enqueue_element():
    num=int(input("Enter element: "))
    queue.append(num)
    print(num," is added to the queue.")

def dequeue_element():
    if is_empty():
        print("Oops! Nothing to remove, queue is empty.")
    else:
        num=queue.pop(0)
        print(num," removed from queue successfully!")
        
def peek_element():
    if is_empty():
        print("Queue is empty!")
    else:
        print("First Element= ",queue[0])

def display_queue():
    if is_empty():
        print("Queue is empty!")
    else:
        print("Queue (front -> rear): ", " <- ".join(map(str, queue)))
    
def is_empty():
    if queue==[]:
        return True
    else:
        return False

while(n!=5):
    print("1.Enqueue\t2.Dequeue\t3.Peek\t4.Display\t5.Exit\t")
    n=int(input())
    if n==1:
        enqueue_element()
    elif n==2: 
        dequeue_element()
    elif n==3:
        peek_element()
    elif n==4:
        display_queue()
    elif n==5:
        print("Final Queue(front -> rear): ", " <- ".join(map(str, queue)))
        print("Good Bye!!")
    else:
        print("Invalid Choice!!")