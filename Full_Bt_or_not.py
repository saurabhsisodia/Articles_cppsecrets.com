# A full binary tree is a tree in which every node other than the 
# leaves has two children
# to check a tree whether it is full bt or not
# we simply do level order traversal and check if at any level
# there is a node such that node.left==None and node.right!=None
# or vice versa then we return False i.e, not full binary tree.

# time complexity of below code is O(n),n=number of nodes

# importing double ended queue 
# to store level's node
from collections import deque
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class Full_Bt(object):
	def __init__(self,root):
		self.root=root
		self.q=deque()

	# if any node exits such that it has only one child ,
	# then this function will return False
	def check_full_bt(self):
		if self.root==None:
			return True
		self.q.append(self.root)
		while len(self.q):
			node=self.q.popleft()
			if node.left==None and node.right:
				return False
			if node.right==None and node.left:
				return False
			if node.left and node.right:
				self.q.append(node.left)
				self.q.append(node.right)
		return True

if __name__=="__main__":
	root=new_node(1)
	root.left=new_node(2)
	root.right=new_node(3)
	root.left.left=new_node(4)
	root.left.right=new_node(5)
	root.right.left=new_node(6)
	obj=Full_Bt(root)
	check=print(obj.check_full_bt())
	if check:
		print("given binary tree is full binary tree")
	else:
		print("not full binary tree")
