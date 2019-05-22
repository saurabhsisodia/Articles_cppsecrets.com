# Python program to find the sum of leaf nodes at minimum level
# to find the sum ,we can do level order traversal and with traversal we can sum up all the leaves at the first occurred 
# level and return, no need to traverse whole tree.

# time complexity is O(n)
# space complexity is O(n)

# importing double ended queue
from collections import deque
# creating new node
class new_node(object):
    def __init__(self,value):
        self.value=value
        self.left,self.right=None,None

class BT(object):
    def __init__(self,root):
        self.root=root
        self.d=deque()
    
     # this function will return sum at minimum level
    def Minimum_level_sum(self):
        # base case
        if root==None:
            return 
        self.d.append(root)
        m_level=0
        x=False
        # iterate for all the nodes
        while len(self.d):
            # count is storing number of nodes at a particular level
            count=len(self.d)
            while count:
                node=self.d.popleft()
                # if leaf node is founded the add it to sum 
                # and set x to true bcoz this level is our minimum level
                # as it is founded first
                if node.left==None and node.right==None:
                    m_level+=node.value
                    x=True
                # iterate for left and right subtree
                if node.left:
                    self.d.append(node.left)
                if node.right:
                    self.d.append(node.right)
                count-=1
            if x:
                return m_level
if __name__=="__main__":
    root=new_node(1)
    
    root.left=new_node(2)
    root.right=new_node(3)
    root.left.left=new_node(4)
    root.left.right=new_node(5)
    root.left.right.left=new_node(3)
    
    root.right.left=new_node(6)
    root.right.right=new_node(7)
    root.right.left.left=new_node(8)
    root.right.left.right=new_node(9)
    
    obj=BT(root)
    print(obj.Minimum_level_sum())

output:: sum is 11
