#Python program to check if a binary tree is subtree of another binary tree

# to check if a tree is a subtree of another tree,
# we can use the fact that inorder and preorder traversal uniquely
# defined a binary tree.
# in place of preorder we can also use postorder traversal 
# first we are doing inorder and preorder traversal of both the trees 
# and store them in arrays of string
# if inorder and preorder traversal of a tree is subarray of another tree 
# then first one is subtree of second.
# time complexity of this algorithm is O(n)
# and space complexity is also O(n)

class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class Subtree(object):
	def __init__(self,root1,root2):
		self.root1=root1
		self.root2=root2

	# function for inorder traversal of tree
	# store it in path array 

	def Inorder_Traversal(self,root,path):
		if root==None:
			return 
		else:
			self.Inorder_Traversal(root.left,path)
			path.append(str(root.value))
			self.Inorder_Traversal(root.right,path)

	# function for preorder traversal of tree
	# store it in path array
	def Preorder_Traversal(self,root,path):
		if root==None:
			return 
		else:
			path.append(str(root.value))
			self.Preorder_Traversal(root.left,path)
			self.Preorder_Traversal(root.right,path)

	# function which will return true if one is subtree of another one
	def check_subtree(self,root1,root2):
		# auxiliary arrays
		tree1_inorder=[]
		tree2_inorder=[]
		tree1_preorder=[]
		tree2_preorder=[]
		self.Inorder_Traversal(root1,tree1_inorder)
		self.Inorder_Traversal(root2,tree2_inorder)
		self.Preorder_Traversal(root1,tree1_preorder)
		self.Preorder_Traversal(root2,tree2_preorder)
		# converting arrays into string to check substring efficiently
		tree1_inorder=''.join(tree1_inorder)
		tree2_inorder=''.join(tree2_inorder)
		tree1_preorder=''.join(tree1_preorder)
		tree2_preorder=''.join(tree2_preorder)
		# if inorder traversal of roo2 tree is not substring of root1 tree
		# then return false 
		if tree1_inorder.find(tree2_inorder)==-1:
			return False
		if tree1_preorder.find(tree2_preorder)==-1:
			return False
		# else return True
		return True

if __name__=="__main__":
	# Original tree
	root1=new_node(5)
	root1.left=new_node(0)
	root1.right=new_node(8)
	root1.left.left=new_node(1)
	root1.left.right=new_node(2)
	#root1.right.left=new_node(6)
	#root1.right.right=new_node(7)
	# another tree

	root2=new_node(5)
	root2.left=new_node(0)
	root2.right=new_node(8)
	obj=Subtree(root1,root2)
	c=obj.check_subtree(root1,root2)
	if c:
		print("tree with root value %d is subtree of original tree with root value %d " %(root2.value,root1.value))
	else:
		print("not subtree")







