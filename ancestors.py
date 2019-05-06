#Python program to print all Ancestors of a given node
# To get all the ancestors of a node ,we can simply print the root to node 
# path in reverse order leaving behind the given node

# defining class to create a new node 
class node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None
class Ancestors(object):
	def __init__(self,root):
		self.root=root
	#function which will store path in array and return true if path exists else False
	def Root_Node_Path(self,root,array,k):
		# Base case
		if root==None:
			return False
		#store current node in array
		array.append(root.value)
		#check if key is same as current node's key
		if root.value==k:
			return True
		# check if key is in left of right subtree 
		if (root.left!=None and self.Root_Node_Path(root.left,array,k) or root.right!=None and self.Root_Node_Path(root.right,array,k)):
			return True
		# if key is not present in the subtree rooted with current root node
		# then remove the current node from the array and return false
		array.pop()
		return False
	# function to print ancestors series
	def Print_Ancestors(self,k):
		# path will store ancestor list
		path=[]
		# check if node(key) is present in tree or not
		if not self.Root_Node_Path(self.root,path,k):
			return -1
		else:
			return path

if __name__=="__main__":

	root=node(4)
	root.left=node(2)
	root.right=node(6)
	root.left.left=node(1)
	root.left.right=node(3)
	root.right.left=node(5)
	root.right.right=node(7)
	obj=Ancestors(root)
	key=int(input())
	check=obj.Print_Ancestors(key)
	if check==-1:
		print("key is not present in tree")
	elif len(check)==1:
		print("given key is root of the tree ")
	else:
		print(*check[::-1][1:])

'''  in above algorithm tree is traversed only ones
	so total time complexity is O(n) ,n=no of nodes.
	Above algorithm requires extra space to store path.'''

