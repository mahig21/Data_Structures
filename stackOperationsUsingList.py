print("Stack operations using list in python")
n=0
stack=[]

def push_element():
    print("Enter the element to push in stack: ")
    num=int(input())
    stack.append(num)
    print("Pushed element: ",num)
    
def pop_element():
    if is_empty():
        print("Oops! Nothing to pop, stack is empty")
    else:
        num=stack.pop()
        print("The element popped is ",num)

def peep_element():
    if is_empty():
        print("Stack is empty!")
    else:
        print("Top= ",stack[-1])

def display_stack():
    if is_empty():
        print("Stack is empty!")
    else:
        print("Stack (top → bottom):")
        print(stack[::-1])

def is_empty():
    if stack==[]:
        return True
    else:
        return False
        
while(n!=5):
    print("1.Push\t2.Pop\t3.Peep\t4.Display\t5.Exit")
    print("Please enter your choice: ")
    n=int(input())
    if n==1:
        push_element()
    elif n==2:
        pop_element()
    elif n==3:
        peep_element()
    elif n==4:
        display_stack()
    elif n==5:
        print("Good Bye!")
    else:
        print("Invalid Choice!")



