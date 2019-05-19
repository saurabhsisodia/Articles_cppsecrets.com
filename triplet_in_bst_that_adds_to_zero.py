# Python program to find if there is a triplet in a Balanced binary search tree that adds to zero

# to check triplet , we just save inorder traversal of the tree in array
# and interate through array for each value and find pair sum in O(n) which will
# give zero on adding with iterate value
# time complexity: O(n2)
# space complexity:O(n)

# creating new node
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class Balanced_BST(object):
	def __init__(self,root):
		self.root=root

	# store inorder traversal of the array
	def Inorder(self,root,array):
		if root:
			self.Inorder(root.left,array)
			array.append(root.value)
			self.Inorder(root.right,array)

	# check if there is a pair which sum up zero with key
	def Check_Pair(self,array,start,end,key):
		while start<end:
			if array[start]+array[end]+key==0:
				return True
			elif array[start]+array[end]+key>0:
				end-=1
			else:
				start+=1
		return False

	# return true for atleat one triplet
	def Check_Triplet(self):
		array=[]
		self.Inorder(self.root,array)
		print(array)
		for i in range(0,len(array)-2):
			check=self.Check_Pair(array,i+1,len(array)-1,array[i])
			if check==True:
				return True
		return False

if __name__=="__main__":
	root=new_node(6)

	root.left=new_node(-14)
	root.right=new_node(14)

	root.left.right=new_node(-2)
	root.right.left=new_node(13)
	root.right.right=new_node(15)
	root.right.left.left=new_node(8)

	obj=Balanced_BST(root)
	print(obj.Check_Triplet())



