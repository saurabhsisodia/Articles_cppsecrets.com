# Python program to print path from root to a given node in a binary tree

# to print path from root to a given node
# first we append a node in array ,if it lies in the path 
# and print the array at last


# creating a new node
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class Root_To_Node(object):
	def __init__(self,root):
		self.root=root


	# function to check if current node in traversal 
	# lies in path from root to a given node
	# if yes then add this node to path_array
	def check_path(self,root,key,path_array):
		#base case
		if root==None:
			return False

		# append current node in path_array
		# if it does not lie in path then we will remove it.
		path_array.append(root.value)
		if root.value==key:
			return True

		if (root.left!=None and self.check_path(root.left,key,path_array)) or (root.right!=None and self.check_path(root.right,key,path_array)):
			return True

		#  if given key does not present in left or right subtree rooted at current node
		#  then delete current node from array
		# and return false

		path_array.pop()
		return False

	def Print_Path(self,key):
		path_array=[]
		check=self.check_path(self.root,key,path_array)
		if check:
			return path_array
		else:
			return -1
if __name__=="__main__":
	root=new_node(5)
	root.left=new_node(2)
	root.right=new_node(12)
	root.left.left=new_node(1)
	root.left.right=new_node(3)
	root.right.left=new_node(9)
	root.right.right=new_node(21)
	root.right.right.left=new_node(19)
	root.right.right.right=new_node(25)
	obj=Root_To_Node(root)
	key=int(input())
	x=obj.Print_Path(key)
	if x==-1:
		print("node is not present in given tree")
	else:
		print(*x)
