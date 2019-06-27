#https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        if(self.root):
            temp = self.root
            while():
                if(val<temp.info):
                    if(temp.left):
                        temp = temp.left
                    else:
                        temp.left = Node(val)
                        break;
                else:
                    if(temp.right):
                        temp = temp.right
                    else:
                        temp.right = Node(val)
                        break;
        else:
            self.root = Node(val)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
