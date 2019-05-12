# Python Program to find the closest leaf node from a given node

# important point which we have to keep in our mind is that closest leaf node 
# can either be descendant of the given node or can lie in subtree rooted at one of its ancestors.
# in this algorithm first we have store all ancestors of the given node
# and then find distance which is closest from one of the parent
# again we have find min distance in the subtree rooted at the given node
# we print minimum from both the distances





# creating new node with specific field
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

# binary tree class
class BT(object):
	# initialize the object with root
	def __init__(self,root):
		self.root=root


	# this function will return the min distance in the subtree rooted at a particular node, 
	# to the leaf node 
	def Down_Distance(self,root,d,dmin):
		if root==None:
			return 

		# if leaf node has arrived
		if root.left==None and root.right==None:
			if d<dmin[0]:
				dmin[0]=d
				dmin[1]=root
			return
		# reccure for left and right subtree
		self.Down_Distance(root.left,d+1,dmin)
		self.Down_Distance(root.right,d+1,dmin)

	# store root to given node path
	def Find_Parent(self,root,given_node,array):
		if root==None:
			return False
		# if given node has arraived then return True
		if root==given_node:
			return True
		# append then current node as it can lie in the path
		array.append(root)
		# check if given node lie in left or right subtree
		if (root.left!=None and self.Find_Parent(root.left,given_node,array)) or (root.right!=None and self.Find_Parent(root.right,given_node,array)):
			return True
		# if no the poped the current node and return False
		array.pop()
		return False


	# this function will return min distance from the parents to the closest leaf node
	def Distance_from_parent(self,given_node):
		array=[]
		x=given_node
		dmin=[100000]*2
		check=self.Find_Parent(self.root,given_node,array)
		if check==False:
			print("node is not present in th tree\n")
			return 
		else:

			array=array[::-1]
			self.Down_Distance(given_node,0,dmin)
			for node in array:
				if node.left==x:
					self.Down_Distance(node.right,2,dmin)
				if node.right==x:
					self.Down_Distance(node.left,2,dmin)
				x=node
			return dmin[0],dmin[1].value


if __name__=="__main__":
	root=new_node(1)

	root.left=new_node(2)
	root.right=new_node(3)

	root.left.left=new_node(4)
	root.left.right=new_node(5)
	root.left.left.left=new_node(8)
	root.left.left.left.left=new_node(7)

	root.left.right.left=new_node(10)
	root.left.right.right=new_node(11)
	root.left.right.left.left=new_node(12)
	root.left.right.right.right=new_node(15)

	given_node=root.left.right

	obj=BT(root)
	distance,leaf=obj.Distance_from_parent(given_node)
	print("closest leaf node from %d  is %d and its distance is %d " %(given_node.value,leaf,distance))

