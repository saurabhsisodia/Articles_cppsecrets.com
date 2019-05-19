class new_node(object):
	def __init__(self,value):
		self.value=value
		self.left=None
		self.right=None
class BT(object):
	def __init__(self,root):
		self.root=root

	def Longest_Consecutive(self,root,comp,length,arr):
		if root==None:
			return None

		if root.value==comp:
			length+=1
		else:
			length=1
		arr[0]=max(length,arr[0])
		self.Longest_Consecutive(root.left,root.value+1,length,arr)
		self.Longest_Consecutive(root.right,root.value+1,length,arr)

	def Print_Length(self):
		arr=[0]*2
		self.Longest_Consecutive(self.root,self.root.value,0,arr)
		return arr[0]


if __name__=="__main__":
	root=new_node(6)

	root.right=new_node(10)
	root.right.left=new_node(7)
	root.right.right=new_node(11)
	root.right.right.right=new_node(12)
	root.right.right.right.right=new_node(13)

	obj=BT(root)
	print(obj.Print_Length())
