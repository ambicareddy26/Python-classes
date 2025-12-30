class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(100)
root.left = Node(20)
root.left.left = Node(5)
root.left.right = Node(25)
root.right = Node(110)
root.right.left = Node(105)
root.right.right = Node(120)

class BST:
    def search_element(root,target):
        if root == None:
            return False
        
        if root.data == target:
            return True
        elif target > root.data:
            return BST.search_element(root.right,target)
        else:
            return BST.search_element(root.left,target)
        
    def insert_element(root,element):
        if root == None:
            return Node(element)
        if element < root.data:
            root.left = BST.insert_element(root.left,element)
        else:
            root.right = BST.insert_element(root.right,element)
        return root
    
    def inorder(root):
        if root != None:
            BST.inorder(root.left)
            print(root.data,end = " ")
            BST.inorder(root.right)

print(BST.search_element(root,12))
BST.insert_element(root,150)
BST.inorder(root)