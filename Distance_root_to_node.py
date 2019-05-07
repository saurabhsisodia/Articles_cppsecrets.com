#Python program to find distance from root to given node in a binary tree

# to find the distance between a node from root node
# we simply traverse the tree and check ,is current node lie in the path from root to the given node,
# if yes then we just increment the length by one and follow the same procedure.


class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class Root_To_Node(object):
	def __init__(self,root):
		self.root=root
		# initializing the value of counter by -1
		self.count=-1

	# function which will calculate distance

	def Distance(self,root,key):
		# base case
		if root==None:
			return False
		# increment counter by one,as it can lie in path from root to node
		# if it will not then we will decrement counter  
		self.count+=1
		# if current node's value is same as given node's value
		# then we are done,we find the given node
		if root.value==key:
			return True
		# check if the given node lie in left subtree or right subtree rooted at current node
		# if given node does not lie then this current node does not lie in path from root to given node
		# so decrement counter by one
		if (root.left!=None and self.Distance(root.left,key)) or ( root.right!=None and self.Distance(root.right,key)):
			return True
		self.count-=1
		return False

	# function which will return distance
	def Print_Distance(self,key):
		check=self.Distance(root,key)
		if check==False:
			print("key is not present in the tree")
		else:
			print(" distance of %d from root node is %d " %(key,self.count))


if __name__=="__main__":

	root=new_node(1)
	root.left=new_node(2)
	root.right=new_node(3)
	root.left.left=new_node(4)
	root.left.right=new_node(5)
	root.right.left=new_node(6)
	root.right.right=new_node(7)
	root.right.left.right=new_node(9)
	root.right.left.right.left=new_node(10)
	obj=Root_To_Node(root)
	key=int(input())
	obj.Print_Distance(key)
''' 
  as we are going at each node only ones so time complexity of above algorithm is 
  O(n),n=no of nodes in the tree''' 
