
# create node class
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

# create linked list class
class Sll:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    # this method used to traverse all nodes and print values of each node
    def print(self):
        if self.head is None:
            print("No any values")
        else:
            node = self.head
            while node is not None:
                print(node.value, end="  ")
                node = node.next
            print()
    
    # this method used to achieve insertion
    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            # add node at the beginning
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            # add node at the end
            elif location == -1:
                self.tail.next = newNode
                self.tail = newNode
            # add node at anywhere except the beginning and the end
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    
    # this method used to search value in linked list
    def search(self, searchValue):
        if self.head is None:
            print("No any values")
        else:
            node = self.head
            while node is not None:
                if node.value == searchValue:
                    print("Value Found")
                    return
                node = node.next
            print("Value Not Found")
    
    # this method used to delete a node from linked list
    def delete(self, location):
        # remove node from the beginning
        if location == 0:
            if self.head.next == self.tail.next:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        # remove node from the end
        elif location == -1:
            if self.head.next == self.tail.next:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = None
                self.tail = node
        # remove node from anywhere except the beginning and the end
        else:
            tempNode = self.head
            index = 0
            while index < location-1:
                tempNode = tempNode.next
                index +=1
            nextNode = tempNode.next
            tempNode.next = nextNode.next


# initialize a linked list
linkedList = Sll()

# create two nodes with values using node class
node1 = Node(4)
node2 = Node(9)

# link nodes and head and tail each other
linkedList.head = node1
node1.next = node2
linkedList.tail = node2

# traverse all node and print values
linkedList.print()

# insert a node at the beginning
linkedList.insert(6, 0)
# insert a node at the end
linkedList.insert(6, -1)
# insert a node at the index 1
linkedList.insert(6, 1)

linkedList.print()

# search value 6 in the linked list
linkedList.search(6)

# remove node at the beginning
linkedList.delete(0)
# remove node at the end
linkedList.delete(-1)
# remove node at index 1
linkedList.delete(1)

linkedList.print()