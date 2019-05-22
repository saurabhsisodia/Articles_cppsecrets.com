
# given a binary tree and you have to find the maximum sum leaf to root path 
# to solve this problem check for every path from root to leaf and get the maximum sum path 
# time complexity :O(nh) where n=number of nodes in the tree and h=height of the tree
# as we are going at each node only once and calculate sum of root to leaf path which in worst case is h i.e, height of the 
# binary tree
# space complexity :O(n)


# creating a new node
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left,self.right=None,None

class BT(object):
	# initializing object with root
	def __init__(self,root):
		self.root=root
		self.maximum=0
		self.maximum_path=[]

	# this function will calculate maximum sum path and store it in array maximum_path
	def Maximum_Sum(self,root,path,l):
		# base case
		if root==None:
			return
		# save current node.value in the path array
		path[l]=root.value
		# incrementing l by 1
		l+=1
		# if current node is leaf node then calculate sum of current path and update maximum sum if needed
		if root.left==None and root.right==None:
			if sum(path[:l])>self.maximum:
				self.maximum=sum(path[:l])
				self.maximum_path=path[:l]
		# reccur for left and right subtree
		else:
			self.Maximum_Sum(root.left,path,l)
			self.Maximum_Sum(root.right,path,l)

	# print the path and its value
	def Print_Maximum_sum_path(self):
		path=[0]*100
		self.Maximum_Sum(self.root,path,0)
		print("maximum path sum is %s  and path is %s " %(self.maximum,self.maximum_path))

if __name__=="__main__":
	root=new_node(8)
	root.left=new_node(7)
	root.right=new_node(6)
	root.left.left=new_node(5)
	root.left.right=new_node(4)
	root.right.left=new_node(3)
	root.right.right=new_node(2)
	root.right.right.right=new_node(1)
	root.right.right.left=new_node(10)
	obj=BT(root)
	obj.Print_Maximum_sum_path()
# output:maximum path sum is 26 and path is 8->6->2->10
