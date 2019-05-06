# Python program to find sum of values in each level of binary tree
# importing double ended queue 
from collections import deque

# class to create a new node
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class Level_Sum(object):
	def __init__(self,root):
		self.root=root
		self.d=deque()

# function to get the sum at each level
	def Print_level_sum(self):
		if self.root==None:
			return
		# enqueue root node in the queue(d)
		self.d.append(self.root)
		# level order traversal with the help of queue
		while len(self.d):
			# count is storing the size of the queue when level order traversal of one level finishes.
			count=len(self.d)
			# storing sum at current level
			sum=0

			# Iterating for current nodes in the queue
			while count>0:
				#dequeue the visited node
				node=self.d.popleft()
				# increament the value of sum by adding poped value
				sum+=node.value
				count-=1
				# enqueue left and right children of poped node.
				if node.left:
					self.d.append(node.left)
				if node.right:
					self.d.append(node.right)
			# printing the value of sum at a level
			print(sum)

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
	obj=Level_Sum(root)
	obj.Print_level_sum()



