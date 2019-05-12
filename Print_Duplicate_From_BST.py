# Python program to print duplicate elements from the binary search tree

# In Binary Search Tree, if there is any duplicates then they will
# come consecutive in Inorder Traversal.
# so we can use this fact and store traversal in a dictionary
# so , whenever we find any element which is already on dictionary
# then we print it,Using Dictionary will take O(1)
# time for searching an element
# Overall complexity of the algorithm is O(n) with O(n)
# space complexity.

from collections import defaultdict
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class BST(object):
	def __init__(self,root):
		self.root=root
		self.d=defaultdict(int)


	# function for inorder traversal and store values
	# in dictionary
	def Print_Duplicate(self,root):
		if root:
			self.d[root.value]+=1
			self.Print_Duplicate(root.left)
			self.Print_Duplicate(root.right)


	# function to print duplicates values
	def Print(self):
		for key in self.d:
			if self.d[key]>1:
				print(key,end=' ')

if __name__=="__main__":
	root=new_node(10)
	root.left=new_node(5)
	root.right=new_node(15)
	root.left.left=new_node(3)
	root.left.right=new_node(7)
	root.right.left=new_node(13)
	root.right.right=new_node(15)
	root.left.left.left=new_node(2)
	root.left.left.right=new_node(4)
	root.left.right.left=new_node(7)
	root.left.right.right=new_node(7)
	root.right.left.left=new_node(12)
	root.right.left.right=new_node(14)
	root.right.right=new_node(15)
	obj=BST(root)
	obj.Print_Duplicate(root)
	obj.Print()
