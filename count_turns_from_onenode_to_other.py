# Python program to count number of turns to reach from one node to another in BT.

# to find the number of turns, we have to calculate turns from the
# lowest common ancestor.
# in this algorithm first i have store path from root to given nodes in two arrays
# then find the index of lowest common ancestor
# then find the number of turns from the LCA, for this i have fill two arrays in such a way
# that they will store left or right direction from LCA
# at the end i have printed the total number of different directions 


# Time complexity::O(n), n=no of nodes in tree
# Space Complexity::O(n)

# create a new node
class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None

class Binary_Tree(object):
	def __init__(self,root):
		self.root=root

	# this function will store root to given node path in array
	def Path(self,root,key,array):
		if root==None:
			return False

		array.append(root)
		if root.value==key:
			return True
		if (root.left and self.Path(root.left,key,array)) or (root.right and self.Path(root.right,key,array)):
			return True

		array.pop()
		return False

	# this function is counting number of turns
	def Turns(self,key1,key2):

		# declaring two arrays to store paths
		array1,array2=[],[]

		# declaring two arrays to store directions
		d1,d2=[],[]

		# checking if both nodes are present in the tree
		check1=self.Path(self.root,key1,array1)
		if check1==False:
			print("key1 is not present in the tree\n")
			return 
		check2=self.Path(self.root,key2,array2)
		if check2==False:
			print("key2 is not present in the tree\n")
			return 
		else:

			# finding index of lowest common ancestor
			i=0
			count=0
			while i<len(array1) and i<len(array2) and array1[i]==array2[i]:
				if array1[i]!=array2[i]:
					break
				i+=1
			index=i-1

			l1=len(array1)
			l2=len(array2)

			# if root node is LCA 
			# the direction doesn't matter at all so put anything here except left or right
			if l1==1:
				d1.append("any")
			if l2==1:
				d2.append("any")

			# store the directions in d1 and d2 arrays
			for i in range(l1-1):
				if array1[i].left==array1[i+1]:
					d1.append("left")
				else:
					d1.append("right")
			d1.append("any")
			for j in range(l2-1):
				if array2[j].left==array2[j+1]:
					d2.append("left")
				else:
					d2.append("right")
			d2.append("any")
			j=index

			# counting number of turns from LCA to nodes separately
			while j<len(d1)-1:
				if d1[j]!=d1[j+1] and d1[j+1]!="any":
					count+=1
				j+=1

			j=index
			while j<len(d2)-1:
				if d2[j]!=d2[j+1] and d2[j+1]!="any":
					count+=1
				j+=1
				
			# if  nodes present in left and right subtree of LCA then add 1 to count  
			if d1[index]!=d2[index] and d1[index]!="any" and d2[index]!="any":
				count+=1
			print(index)
			print(d1,d2)
			print(count)

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
	key1,key2=map(int,input().split( ))
	obj=Binary_Tree(root)
	obj.Turns(key1,key2)
