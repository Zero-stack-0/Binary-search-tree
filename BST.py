class Node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.val=key
def insert(root,key):
    if(root is None):
        return(Node(key))
    else:
        if(root.val<key):
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return(root)
def inorder(root):
    if(root):
        inorder(root.left)
        print(root.val)
        inorder(root.right)
r=Node(50)
r=insert(r,40)
r=insert(r,30)
r=insert(r,20)
r=insert(r,10)
r=insert(r,60)
r=insert(r,90)
inorder(r)