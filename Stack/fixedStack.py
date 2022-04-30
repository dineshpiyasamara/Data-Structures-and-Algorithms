class Stack:
    def __init__(self, size):
        self.size = size
        self.list = []
    
    def __str__(self):
        return str(self.list)
    
    # isEmpty()
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    # isFull()
    def isFull(self):
        if len(self.list) == self.size:
            return True
        else:
            return False
    
    # push()
    def push(self, value):
        if self.isFull():
            return "Stack is full"
        else:
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
