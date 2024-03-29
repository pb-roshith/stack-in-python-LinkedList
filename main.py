class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top is None
    
    def StackPush(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new
        
    def StackPop(self):
        if self.top == None:
            return "Stack is empty"
        p = self.top.data
        self.top = self.top.next
        return p
    
    def peek(self):
        if self.top == None:
            return "Stack is empty"
        return self.top.data
        
    def traverse(self):
        curr = self.top
        while curr:
            print(curr.data,end="->")
            curr = curr.next
        print("None")
        
stack = Stack()
stack.StackPush(10)
stack.StackPush(20)
stack.StackPush(30)
stack.StackPush(40)
print(stack.peek())
print(stack.isEmpty())
print(stack.StackPop())
print(stack.StackPop())
stack.traverse()
