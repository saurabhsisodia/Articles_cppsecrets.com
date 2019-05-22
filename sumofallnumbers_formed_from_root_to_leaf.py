# Python program to find the sum of all numbers that are formed from root to leaf path


# to find the sum of all these numbers,first we are storing root to leaf path in an array
# and then converting path into number by join method of str
# and after that sum up all these numbers and store sum in variable summation

# create a new node
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left,self.right=None,None

class BT(object):
	# initializing object by root and summation=0
	def __init__(self,root):
		self.root=root
		self.summation=0

	# this function will store root to leaf path in an array and convert it into number 
	# and then add them.
	def Root_To_Leaf(self,root,path,l):

		# base case
		if root==None:
			return 
		# add current node in the path array in the form of string	
		path[l]=str(root.value)
		# increment length by one 
		l+=1
		#if current node is leaf node then we get a path from root to leaf
		# so convert it into number and add the number into summation 
		if root.left==None and root.right==None:
			self.summation=self.summation+int(''.join(path[:l]))

		# reccur for left and right subtree
		else:
			self.Root_To_Leaf(root.left,path,l)
			self.Root_To_Leaf(root.right,path,l)


	# this function will print the sum of all the numbers as formed from a path
	def Print_Sum(self):
		path=[0]*100
		self.Root_To_Leaf(self.root,path,0)
		print(self.summation)



if __name__=="__main__":
	root=new_node(1)

	root.left=new_node(2)
	root.right=new_node(3)

	root.left.left=new_node(4)
	root.left.right=new_node(5)
	root.right.left=new_node(6)
	root.right.right=new_node(7)
	obj=BT(root)
	obj.Print_Sum()

# output::    522
