#Python program to get level of a node in binary tree using recursion

#Level of a specific node is the length of the path from root to that node.
#root is at level 0


# class to create a node with specified fields.
class node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

# class to perform operations on the created tree.
class Level_Class(object):

	# Initialization of Instance with root node 
	def __init__(self,root):
		self.root=root

	# As recursion stores argument's  at each recursive call,
	# so we can take advantage of this fact.
	# If there are two nodes of same node.value then,
	# this function will give level of first occurrence only.
	def get_level(self,root,data,start):
		if root==None:
			return 
		if root.value==data:
			return start
		return self.get_level(root.left,data,start+1) or self.get_level(root.right,data,start+1)

if __name__=="__main__":
	root=node(1)
	root.left=node(2)
	root.right=node(3)
	root.left.left=node(4)
	root.left.right=node(5)
	root.right.left=node(6)
	root.right.right=node(7)
	obj=Level_Class(root)

	# node.value whose level is required

	data=int(input())

	# as level of the root node is 0,
	# so starting value of start is 0.
	l=obj.get_level(root,data,0)
	if l==None:
		print("value is not present in tree")
	else:
		print(l)
'''
   as we are going at every node to find the specific node,so
   worst case time complexity of above algorithm is O(n),
   where n is no of nodes in tree.'''


