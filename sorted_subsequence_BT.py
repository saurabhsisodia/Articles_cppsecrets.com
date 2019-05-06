#Python program to check if given sorted sub-sequence exists in binary search tree

# the idea used behind this algorithm is that,we do inorder traversal
# of the bst, as the given sequence is sorted(in ascending order) so we can check every element with the current inordered element
# if it is founded the just poped that element from seq , we will follow 
# this procedure till end 
# after inorder traversal if seq is empty that means all elements has been founded
# by doing this the overall time complexity for algorithm will be O(n).


# class to create a new node
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class BST(object):
	def __init__(self,root):
		self.root=root

	# this function will poped 0 th item from the seq if it is founded in inorder traversal of bst
	def check_seq(self,root,seq):
		# base case
		if root==None:
			return 
		# go to the left subtree.	
		self.check_seq(root.left,seq)
		# if current node.value is same as first element in seq,then we find the first item 
		# so poped it 
		if len(seq)!=0 and root.value==seq[0] :
			seq.popleft()
		# go to the right subtree .
		self.check_seq(root.right,seq)

if __name__=="__main__":
	from collections import deque
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

	# take input, it must be sorted
	seq=list(map(int,input().split( )))

	# storing the given sequence in deque so that popleft can be done in O(1) time.
	d=deque(seq)
	obj.check_seq(root,d)

	# if after inorder traversal ,deque is empty then we are done ,otherewise sequence is not present in bst.
	if len(d)==0:
		print("founded")
	else:
		print("not founded") 

