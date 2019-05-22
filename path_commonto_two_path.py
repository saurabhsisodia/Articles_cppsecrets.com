# Python program to print the path common to the two paths from the root to the two given nodes

# to find the common path between two nodes in a binary tree
# first we are finding lowest common ancestor of two nodes and then we are printing path from node to lowest 
# common ancestor
# as we are going to every node twice so 
# time complexity is O(n)
# space complexity is also O(n)   



class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class BT(object):
	def __init__(self,root):
		self.root=root

	def Find_Path(self,root,path_array,key):
		if root==None:
			return False

		path_array.append(root.value)
		if root.value==key:
			return True

		if (root.left and self.Find_Path(root.left,path_array,key)) or ( root.right and self.Find_Path(root.right,path_array,key)):
			return True

		path_array.pop()
		return False

	def Print_Common_Path(self,key1,key2):
		array1,array2=[],[]
		check1=self.Find_Path(self.root,array1,key1)
		if check1==False:
			print("key is not present")
			return 
		check2=self.Find_Path(self.root,array2,key2)
		if check2==False:
			print("no key ")
			return

		i=0
		while array1[i]==array2[i]:
			print(array1[i], end=' ')
			i+=1


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
	key1,key2=map(int,input().split( ))
	obj.Print_Common_Path(key1,key2)
