# Python program to find the distance between two nodes.

# to find the distance between two nodes ,
# first we find the root to node path of each node 
# then compare both paths and sum up all the nodes after lowest common ancestor
# in both paths.
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class Node_Node_Distance(object):
	def __init__(self,root):
		self.root=root

	def get_path(self,root,array,node):
		# Base case
		if root==None:
			return False
		#store current node in array
		array.append(root.value)
		#check if node is same as current node's key
		if root.value==node:
			return True
		# check if key is in left of right subtree 
		if (root.left!=None and self.get_path(root.left,array,node)) or (root.right!=None and self.get_path(root.right,array,node)):
			return True
		# if key is not present in the subtree rooted with current root node
		# then remove the current node from the array and return false
		array.pop()
		return False
	# function to print distance
	def Print_Distance(self,node1,node2):
		# defining array to store paths 
		array1=[]
		array2=[]
		# if either node1 or node2 does not present in tree then return -1
		if not self.get_path(self.root,array1,node1) or not self.get_path(self.root,array2,node2):
			return -1
		#compare the paths to get first different value 

		i=0
		while i<len(array1) and i<len(array2):
			if array1[i]!=array2[i]:
				break
			i+=1
		# return sum of nodes after lowest common ancestor from both paths.
		return len(array1[i:])+len(array2[i:])

if __name__=="__main__":

	root=new_node(1)
	root.left=new_node(2)
	root.right=new_node(3)
	root.left.left=new_node(4)
	root.left.right=new_node(5)
	root.right.left=new_node(6)
	root.right.right=new_node(7)
	root.right.left.right=new_node(9)
	root.right.left.right.left=new_node(10)
	obj=Node_Node_Distance(root)
	node1,node2=map(int,input().split( ))
	x=obj.Print_Distance(node1,node2)
	if x==-1:
		print("invalid nodes")
	else:
		print(x)
