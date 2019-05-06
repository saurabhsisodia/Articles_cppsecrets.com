# python program to check if a tree is sorted level wise or not

# Importing double ended queue from collections module
# this program will return the first level which is unsorted.
from collections import deque
#creating new_node
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None
# creating class to perfrom operations on tree
class Level(object):
	def __init__(self,root):
		self.root=root
		self.q=deque()
		self.list=[]
	def level_traversal(self):
		# if tree is Null then return 
		if root==None:
			return None
		# enqueue root node in the queue
		self.q.append(root)
		#level variable will keep track of each level
		level=-1
		while len(self.q):
			level+=1
			# count is storing the size of the queue when level order traversal of one level finishes.
			count=len(self.q)
			self.list=[]
			while count>0:
				# poped the current visited node
				node=self.q.popleft()
				#append poped node in the list
				self.list.append(node.value)
				#enqueue left and right children of the poped node.
				if node.left:
					self.q.append(node.left)
				if node.right:
					self.q.append(node.right)
				count-=1
			#function which will check the sequence at each leve sorted or not
			check=self.Check_Sorted(self.list)
			if check==False:
				return level
		return -1
	def Check_Sorted(self,array):
		if len(array)==1:
			return True
		l=len(array)
		for i in range(l-1):
			if array[i+1]<array[i]:
				return False
		return True


if __name__=="__main__":
	root=new_node(2)
	root.left=new_node(7)
	root.right=new_node(5)
	root.left.left=new_node(2)
	root.left.right=new_node(6)
	root.right.right=new_node(9)
	root.left.right.left=new_node(5)
	root.left.right.right=new_node(11)
	root.right.right.left=new_node(4)
	obj=Level(root)
	# variable lev is storing the level returned by level_traversal function
	#if lev=-1,then all levels are sorted
	lev=obj.level_traversal()
	if lev==-1:
		print("tree is sorted level wise")
	elif lev>=0:
		print("tree is unsorted at level %d" %(lev))
	else:
		print(" empty tree")


		
