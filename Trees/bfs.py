from queue import Queue

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def bfs(root):
        q = Queue()
        q.put(root)
        while q.qsize() > 0:
            curr = q.get()
            print(curr.data,end = " ")
            if curr.left != None:
                q.put(curr.left)
            if curr.right != None:
                q.put(curr.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(50)
root.left.left = Node(40)



Tree.bfs(root)