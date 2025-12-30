class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(50)
root.left.left = Node(40)

class Tree:
    def inorder(root):
        if root != None:
            Tree.inorder(root.left)
            print(root.data,end = " ")
            Tree.inorder(root.right)

    def preorder(root):
        if root != None:
            print(root.data,end = " ")
            Tree.preorder(root.left)
            Tree.preorder(root.right)

    def postorder(root):
        if root != None:
            Tree.postorder(root.left)
            Tree.postorder(root.right)
            print(root.data,end = " ")

    def ri_r_l(root):
        if root != None:
            Tree.ri_r_l(root.right)
            print(root.data,end = " ")
            Tree.ri_r_l(root.left)

    def r_ri_l(root):
        if root != None:
            print(root.data,end = " ")
            Tree.r_ri_l(root.right)
            Tree.r_ri_l(root.left)

    def ri_l_r(root):
        if root != None:
            Tree.ri_l_r(root.right)
            Tree.ri_l_r(root.left)
            print(root.data,end = " ")

print("Inorder traversal:")
Tree.inorder(root)
print("\n")
print("Preorder traversal:")
Tree.preorder(root)
print("\n")
print("Postorder traversal:")
Tree.postorder(root)
print("\n")
print("Right Root Left:")
Tree.ri_r_l(root)
print("\n")
print("Root Right Left:")
Tree.r_ri_l(root)
print("\n")
print("Right Left Root:")
Tree.r_ri_l(root)

