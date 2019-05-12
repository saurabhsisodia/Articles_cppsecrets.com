
# to count all the pairs with given sum in different bst
# we use the fact that inorder traversal of bst always gives sorted sequence
# so we store inorder traversal of both bst in arrays
# then traverse arrays i.e, traverse first array from start and second array from end 
# if we array1[start]+array2[end]==sum then count+=1 and star+=1,end-=1
# if array1[start]+array2[end]>sum then we have reduce this value which is possible only by decrementing end by 1
# if calculated sum is less then given sum then we have to increase the sum by incrementing start by 1
# space complexity =O(n)
# time complexity =O(n)
# we can also solve this problem by hash data structure 
class new_node(object):
	# Initializing a node
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class BST(object):
	def __init__(self,root1,root2):
		self.root1=root1
		self.root2=root2
		self.array1=[]
		self.array2=[]

	# doing inorder traversal of the tree
	def Inorder_Traversal(self,root,array):
		if root:
			self.Inorder_Traversal(root.left,array)
			array.append(root.value)
			self.Inorder_Traversal(root.right,array)
		
	def count_Pairs(self,given_sum):
		self.Inorder_Traversal(self.root1,self.array1)
		self.Inorder_Traversal(self.root2,self.array2)
		# start points to starting of array1
		# end points to ending of array2
		start,end=0,len(self.array2)-1
		count=0
		# if one array is traversed whole then stop
		while start<len(self.array1) and end>=0:
			# if sum if founded then count++ and increase both start and end
			if self.array1[start]+self.array2[end]==given_sum:
				count+=1
				start+=1
				end-=1
			elif self.array1[start]+self.array2[end]>given_sum:
				end-=1
			else:
				start+=1
		return count

if __name__=="__main__":
	# first binary search tree
	root1=new_node(8)
	root1.left=new_node(3)
	root1.right=new_node(10)
	root1.left.left=new_node(1)
	root1.left.right=new_node(6)
	root1.left.right.left=new_node(5)
	root1.left.right.right=new_node(7)
	root1.right.right=new_node(14)
	root1.right.right.left=new_node(13)

	# second binary search tree
	root2=new_node(5)
	root2.left=new_node(2)
	root2.right=new_node(18)
	root2.left.left=new_node(1)
	root2.left.right=new_node(3)
	root2.left.right.right=new_node(4)
	root2.right=new_node(18)

	obj=BST(root1,root2)
	given_sum=int(input())  # enter sum which u have to find
	print(obj.count_Pairs(given_sum))

''' OUTPUT:: pairs with sum 10 are::
     	(5,5)
     	(6,4)
     	(7,3)
     	(8,2)
'''

