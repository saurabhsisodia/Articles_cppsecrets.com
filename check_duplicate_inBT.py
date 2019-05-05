# Python program to check if a binary tree has duplicate values

# Create hash table by using defaultdict module of collections package and initialize it with 0(int)
from collections import defaultdict
hash_table=defaultdict(int)

class New_Node(object):
	#constructor to create new node with given data/value,left and right pointer as NULL
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

# preorder traversal of tree

def preorder(root):
	if root:
		print(root.value,end=' ')
		preorder(root.left)
		preorder(root.right)

def Check_Duplicate(root,hash_table):

	# for empty tree
	if root==None:
		return False

	# if value is already present in hash_table

	if hash_table[root.value]:
		return True

	# insert current node's data in hash_table

	hash_table[root.value]=1

	# recursively called the function for left and right subtree

	return Check_Duplicate(root.left,hash_table) or Check_Duplicate(root.right,hash_table)

# Driver Code
if __name__=="__main__":
	root =New_Node(15)
	root.left =New_Node(10)
	root.right =New_Node(32)
	root.left.left =New_Node(4)
	root.left.right =New_Node(9)
	root.left.left.left =New_Node(46)
	root.left.left.right =New_Node(15)
	print("preorder traversal of binary tree is:: ")
	preorder(root)
	print("\n")
	if Check_Duplicate(root,hash_table):
		print("it has duplicate values")
	else:
		print("no duplicate values")

''' OUTPUT::
    preorder traversal of binary tree is ::

    15 10 4 46 15 9 32
    it has duplicate values '''
