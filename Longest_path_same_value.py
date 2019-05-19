# Python program to find longest path with same values in a binary tree
                           6
                              \
                                10
                               /     \
                             7        10
                                           \
                                            10
                                               \
                                                 10
# in above tree longest path with same values has length 4 i.e,10->10->10->10


# to find the longest path, we can compare every node's value 
# to its parent node value , if it is equal to then  increment length by 1
# time complexity : O(n)
# space complexity:O(1)

# creating new node
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None
class BT(object):
	def __init__(self,root):
		self.root=root
         # this function will save longest length
	def Longest_Path(self,root,comp,length,arr):
                # base case
		if root==None:
			return None
               # if current node.value is same as  parent value  then add 1 to length
		if root.value==comp:
			length+=1
		else:
			length=1
                 # storing maximum length in arr
		arr[0]=max(length,arr[0])
		self.Longest_Path(root.left,root.value,length,arr)
		self.Longest_Path(root.right,root.value,length,arr)
         # print longest length
	def Print_Length(self):
		arr=[0]*2
		self.Longest_Path(self.root,self.root.value,0,arr)
		return arr[0]


if __name__=="__main__":
	root=new_node(6)

	root.right=new_node(10)
	root.right.left=new_node(7)
	root.right.right=new_node(10)
	root.right.right.right=new_node(10)
	root.right.right.right.right=new_node(10)

	obj=BT(root)
	print(obj.Print_Length())
