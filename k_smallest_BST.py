
	#Python program to find k-th smallest element in binary search tree
'''
	To find the k th smallest element in bst,we traverse the bst and store it's inorder traversal
	then we print the k th element from the list.'''


'''  this algorithm takes O(n) time complexity and O(n) extra space.
	we can improve time complexity by storing rank of each node i.e By implementing the Augmented Data Structure,
	which will give O(h) time where h=height of the tree.

	We will discuss more efficient solution in next post.
'''	
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None


class bst_operation(object):
	def __init__(self,root):
		self.root=root
		self.storage=[]				# to store node.value

	def Inorder_walk(self,root):     # this procedure will take O(n) time.
		if root==None:
			return
		self.Inorder_walk(root.left)
		self.storage.append(root.value)
		self.Inorder_walk(root.right)

	def get_kth_minimum(self,k):     # O(1) time 
		return self.storage[k-1]


if __name__=="__main__":
	root=new_node(15)
	root.left=new_node(6)
	root.right=new_node(18)
	root.left.left=new_node(3)
	root.left.right=new_node(7)
	root.right.left=new_node(17)
	root.right.right=new_node(20)
	root.left.left.left=new_node(1)
	root.left.left.right=new_node(4)
	root.left.right.right=new_node(13)
	root.left.right.right.left=new_node(9)
	obj=bst_operation(root)
	obj.Inorder_walk(root)
	print("entre value of k::")
	k=int(input())                   # k<=n where n=no of nodes in the tree
	print("%sth smallest element in given binary search tree is %s " %(k,obj.get_kth_minimum(k)))
