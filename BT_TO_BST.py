# Python program to convert binary tree to binary search tree

''' As binary search tree is a binary tree which has following properties--
       1::left subtree of a node contains only nodes which have node.data lesser than node's data.
       2::right subtree of a node contains only nodes which have node.data greater than node's data.
       3::there must be no duplicate nodes. 


	To convert a binary tree into a binary search tree, we follow following steps--
		1..traverse the binary tree and store it's node.data into an array.
		2..sort the array.
		3..again do inorder traversal of the tree and store the array elements to tree's nodes one by one.
	Here, Original structure of binary tree will remain same.
'''		


from collections import deque  #importing double ended queue so that we can do pop and append operation in O(1) time complexity.
class new_node(object):
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def Store_Inorder_Traversal(root,array): #function to store the inorder traversal of tree into an auxiliary array.
										 # it will take O(n) time{n=no of nodes in tree} . 
	if root==None:
		return
	Store_Inorder_Traversal(root.left,array)
	array.append(root.data)
	Store_Inorder_Traversal(root.right,array)
def Bt_to_Bst(root,array):   # main function which will store array elements into the tree.
							 #  O(n) time 
	if root==None:
		return
	Bt_to_Bst(root.left,array)
	root.data=array[0]
	array.popleft()          # if we use list in place of deque then poping an element from left side will takes O(n) time.
	Bt_to_Bst(root.right,array)
def Inorder_Traversal(root):
	if root==None:
		return 
	Inorder_Traversal(root.left)
	print(root.data,end=' ')
	Inorder_Traversal(root.right)


if __name__=="__main__":
	root=new_node(8)
	root.left=new_node(7)
	root.right=new_node(6)
	root.left.left=new_node(5)
	root.left.right=new_node(4)
	root.right.left=new_node(3)
	root.right.right=new_node(2)
	root.right.right.right=new_node(1)
	print("inorder_traversal of binary tree::")
	Inorder_Traversal(root)
	array=deque([])
	Store_Inorder_Traversal(root,array)
	array=deque(sorted(array))            # O(nlgn) time complexity to sort the array.
	Bt_to_Bst(root,array)
	print("\n")
	print("inorder traversal of bst::")
	Inorder_Traversal(root)


'''
	given binary tree is::

	       8
	    //   \\ 
	   7       6
	 // \\    // \\
	 5    4   3    2
	               \\
	                 1 
	it's inorder traversal is:: 5 7 4 8 3 6 2 1

	new binary search tree of above binary tree will be::

	       4
	    //   \\ 
	   2       6
	 // \\    // \\
	 1    3   5    7
	               \\
	                 8
	it's inorder traversal is:: 1 2 3 4 5 6 7 8
	
	From above fig..we conclude that using this procedure the original structure of given binary tree will not change.
	Total time complexity will be--
	O(n)+O(n)+O(nlgn)=O(nlgn).
'''
