# Python Program To print the middle level of perfect binary tree without calculating height of tree

# A perfect binary tree is a binary tree in which all interior nodes have two 
# children and all leaves have the same depth or same level.
# we can find the middle level  of a perfect binary tree by using slow and fast pointer reference
# we move slow pointer by 1 and fast pointer by 2
# this algorithm will return level at number floor(h/2)
# root is at level 0.

class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class Middle_Level(object):
	def __init__(self,root):
		self.root=root

	def Print_Middle_Level(self,slow,fast):
		# base case
		if slow==None or fast==None:
			return

		# if fast pointer is at last level then,
		# slow will be at middle level 
		# so print that 
		if fast.left==None and fast.right==None:
			print(slow.value,end=' ')
			return 
		# if fast pointer is at second last level 
		# then it will never reach to last level
		if fast.left.left==None:
			print(slow.value,end=' ')
			return 

		self.Print_Middle_Level(slow.left,fast.left.left)
		self.Print_Middle_Level(slow.right,fast.right.right)


if __name__=="__main__":
	root=new_node(1)
	root.left=new_node(2)
	root.right=new_node(3)
	root.left.left=new_node(4)
	root.left.right=new_node(5)
	root.right.left=new_node(6)
	root.right.right=new_node(7)
	root.left.left.left=new_node(8)
	root.left.left.right=new_node(9)
	root.left.right.left=new_node(10)
	root.left.right.right=new_node(11)
	root.right.left.left=new_node(12)
	root.right.left.right=new_node(13)
	root.right.right.left=new_node(14)
	root.right.right.right=new_node(15)
	root.left.left.left.left=new_node(16)
	root.left.left.left.right=new_node(17)
	root.left.left.right.left=new_node(18)
	root.left.left.right.right=new_node(19)
	root.left.right.left.left=new_node(20)
	root.left.right.left.right=new_node(21)
	root.right.left.left.left=new_node(22)
	root.right.left.left.right=new_node(23)
	root.right.left.right.left=new_node(24)
	root.right.left.right.right=new_node(25)
	root.right.right.left.left=new_node(26)
	root.right.right.left.right=new_node(27)
	root.right.right.right.left=new_node(28)
	root.right.right.right.right=new_node(29)
	obj=Middle_Level(root)
	obj.Print_Middle_Level(root,root)
