# Python program to reverse a path in binary search tree using queue

# to reverse a path from root to a given key in binary search tree ,we can
# directly store root to given node path's address in an queue and reverse the values
# with the help of queue.
# as we are going at each node only once so time complexity is O(n)
# and space complexity is also O(n)

# importing double ended queue from collections module
from collections import deque

# creating new node
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class BST(object):
	# initialize the object with root and queue
	def __init__(self,root):
		self.root=root
		self.d=deque()

    # performing inorder traversal of the tree
	def Inorder(self,root):
		if root:
			self.Inorder(root.left)
			print(root.value,end=' ')
			self.Inorder(root.right)


	# storing root to given key path's address in the queue
	def Root_To_Key(self,root,key,d):
		# base case
		if root==None:
			return False

		# store current node in queue as it may lie in path
		d.appendleft(root)

		# if currentnode's value if equal to key return True
		if root.value==key:
			return True

		# check for the key in left and right subtree of the current root node
		if (root.left and self.Root_To_Key(root.left,key,d)) or ( root.right and self.Root_To_Key(root.right,key,d)):
			return True

		# if it does not lie in path then delete current node from queue and return False
		d.popleft()
		return False


	# this function will reverse the keys in  path
	def Reverse_Path(self,key):

		c=self.Root_To_Key(self.root,key,self.d)

		# if given key is not present in the tree

		if c==False:
			print("key is not present\n")
			return
		# reversing values from queue
		start,end=0,len(self.d)-1
		while start < end:
			self.d[start].value,self.d[end].value=self.d[end].value,self.d[start].value
			start+=1
			end-=1


if __name__=="__main__":
	root=new_node(5)
	root.left=new_node(2)
	root.right=new_node(12)
	root.left.left=new_node(1)
	root.left.right=new_node(3)
	root.right.left=new_node(9)
	root.right.right=new_node(21)
	root.right.right.left=new_node(19)
	root.right.right.right=new_node(25)
	obj=BST(root)
	print("before reverse")
	obj.Inorder(root)
	print("\n")
	key=int(input())
	obj.Reverse_Path(key)
	print("after reverse")
	obj.Inorder(root)
'''

output:: inorder traversal before reverse is :: 1 2 3 5 9 12 19 21 25
      	entre the key :: 9
         inorder traversal after reverse is ::: 1 2 3 9 5 12 19 21 25
'''
