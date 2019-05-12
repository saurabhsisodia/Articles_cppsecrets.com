#Python program to find difference between sums of odd level and even level nodes of a binary tree

# to find difference b/w odd and even level sum
# with the inorder traversal we store level sum in two variable
# sum_even and sum_odd
# whenever level is odd,increment sum_odd else sum_even
# we are using queue data structure to go to every level of the tree.

# importing double ended queue
from collections import deque
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

# binary tree class
class BT(object):
	def __init__(self,root):
		self.root=root
		# ini
		self.q=deque()

	# doing level order traversal in a modified way
	def Difference(self):
		if self.root==None:
			return
		# level variable is initialized with value -1
		# at each level it is incremented by 1
		sum_odd,sum_even,level=0,0,-1
		self.q.append(self.root)
		while len(self.q):
			level+=1
			# count stores the number of nodes at each level
			count=len(self.q)
			while count>0:
				# delete and return first element from the queue
				pop=self.q.popleft()
				# condition for even level 
				if level%2==0:
					sum_even+=pop.value
				else:
					sum_odd+=pop.value
				# appending left and right child of current poped node
				if pop.left:
					self.q.append(pop.left)
				if pop.right:
					self.q.append(pop.right)
				count-=1
		return sum_even,sum_odd
	def Print_Difference(self):
		sum_even,sum_odd=self.Difference()
		print("difference b/w odd level sum and even level sum is %d " %(sum_odd-sum_even))


if __name__=="__main__":
	root=new_node(1)
	root.left=new_node(2)
	root.right=new_node(3)
	root.left.left=new_node(4)
	root.left.right=new_node(5)
	root.right.left=new_node(6)
	root.right.right=new_node(7)
	obj=BT(root)
	obj.Print_Difference()	
