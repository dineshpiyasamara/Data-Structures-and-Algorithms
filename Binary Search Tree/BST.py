class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfully inserted"


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data, end=" ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end=" ")
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end=" ")


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild is not None:
            if rootNode.leftChild.data == nodeValue:
                print("The value is found")
            else:
                searchNode(rootNode.leftChild, nodeValue)
        else:
            print("The value is not found")
    else:
        if rootNode.rightChild is not None:
            if rootNode.rightChild.data == nodeValue:
                print("The value is found")
            else:
                searchNode(rootNode.rightChild, nodeValue)
        else:
            print("The value is not found")


def minValueNode(bstNode):
    current = bstNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode


def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been successfully deleted"

# create
# newBST = BSTNode(None)
# print(newBST.data)


# insert
# newBST = BSTNode(None)
# insertNode(newBST, 6)
# insertNode(newBST, 8)
# print(newBST.data)
# print(newBST.rightChild.data)
# print(newBST.leftChild)


# preorder traversal
# newBST = BSTNode(None)
# insertNode(newBST, 6)
# insertNode(newBST, 4)
# insertNode(newBST, 8)
# insertNode(newBST, 2)
# insertNode(newBST, 5)
# insertNode(newBST, 9)
# insertNode(newBST, 1)
# preOrderTraversal(newBST)
# inOrderTraversal(newBST)
# postOrderTraversal(newBST)


# search
# newBST = BSTNode(None)
# insertNode(newBST, 6)
# insertNode(newBST, 4)
# insertNode(newBST, 8)
# insertNode(newBST, 2)
# insertNode(newBST, 5)
# insertNode(newBST, 9)
# insertNode(newBST, 1)
# searchNode(newBST, 9)
# searchNode(newBST, 7)

# delete
# newBST = BSTNode(None)
# insertNode(newBST, 6)
# insertNode(newBST, 4)
# insertNode(newBST, 8)
# insertNode(newBST, 2)
# insertNode(newBST, 5)
# insertNode(newBST, 9)
# insertNode(newBST, 1)
# preOrderTraversal(newBST)
# deleteNode(newBST, 1)
# preOrderTraversal(newBST)
