class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        return str(self.list)
    
    # isEmpty()
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    # push()
    def push(self, value):
        return self.list.append(value)
    
    # pop()
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list.pop()
    
    # peek()
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list[-1]
    
    # delete()
    def delete(self):
        self.list = None


myStack = Stack()

print(myStack)
print(myStack.isEmpty())

myStack.push(4)
myStack.push(6)
print(myStack)

myStack.pop()
myStack.pop()
print(myStack)

myStack.push(4)
myStack.push(6)
myStack.push(2)
myStack.push(7)
print(myStack)

print(myStack.peek())

myStack.delete()
print(myStack)