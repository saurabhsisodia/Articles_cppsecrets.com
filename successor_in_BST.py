'''

	If all keys are distinct ,the successor of a node x is the node with 
	smallest key greater than x.key.

	If the right subtree of node x is nonempty,then successor of x is just the
	leftmost node in x's right subtree.

	If right subtree of node x is empty and x has a successor y,then y is the 
	lowest ancestor of x whose left child is also an ancestor of x.
'''	 

class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class BST_Operations(object):
	def __init__(self,root):
		self.root=root

	def Get_Minimum(self,root):    # O(h)

		current=root
		while current.left:
			current=current.left

		return current

	def Search(self,key):     # O(h)
		current=self.root
		while current and current.value!=key:
			if current.value>key:
				current=current.left
			else:
				current=current.right
		return current


	def Get_Parent(self,root,data):
		if root:
			if root.left and root.left.value==data:
				return root
			if root.right and root.right.value==data:
				return root

			elif root:
				return self.Get_Parent(root.left,data) or self.Get_Parent(root.right,data)


	# Here,I believe that node is present whose successor we are finding. 
	def Get_Successor(self,key):  # if we know all the parents then this function will run in O(h) time complexity.

		current=self.Search(key)
		if current.right:
			return self.Get_Minimum(current.right)
		else:
			par=self.Get_Parent(root,current.value)
			while par and current==par.right:
				current=par
				par=self.Get_Parent(root,par.value)
			return par

if __name__=="__main__":
	root=new_node(15)
	root.left=new_node(6)
	root.right=new_node(18)
	root.left.left=new_node(3)
	root.left.right=new_node(7)
	root.right.left=new_node(17)
	root.right.right=new_node(20)
	root.left.left.left=new_node(1)
	root.left.left.right=new_node(4)
	root.left.right.right=new_node(13)
	root.left.right.right.left=new_node(9)
	key=int(input())    # whose inorder successor is required
	obj=BST_Operations(root)
	w=obj.Get_Successor(key)
	if w:
		print(w.value)
	else:
		print("no successor") 
