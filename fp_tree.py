# coding=utf-8
import pdb
import string

class Node:#tree sturcture
	def __init__(self):
		self.num_children=0
		self.children=[]
		self.parent=None
		self.times=0
		self.item=''

def stats(filename):#calculate purchased times of every items
	for line in filename:
		for element in line:
			for character in string.lowercase:
				if(element==character):
					temp=ord(character)-97
					sample_list[temp]=sample_list[temp]+1
	return sample_list

def swapping(sample_list,minimum_support):#sort and delete those elements who did not meet the minimum_support
	i=0
	j=0
	new_list=['']*26
	for i in range(0,26):
		temp=0
		temp2=0
		for j in range(0,26):
			if(temp<sample_list[j]):
				temp=sample_list[j]
				temp2=j
		if(temp>=minimum_support):
			new_list[i]=chr(temp2+97)
		sample_list[temp2]=0
	for n in range(0,26):
		if(new_list[-1]==''):
			new_list.remove('')
	return new_list

def ordered_frequent_items(filename, listname):#find the frequent items of users
	file=open('input.txt')
	num_of_line=len(file.readlines())#calculate how many lines in file
	print "num of lines : ", num_of_line
	OFI_list = [[] for i in range(num_of_line)]#avoid shallow copy
	n=0
	file=open('input.txt')
	for line in file:
		print line
		for character in listname:
			for element in line:
				if(character==element):
					OFI_list[n].append(character)
		print OFI_list[n]
		n=n+1
	return OFI_list

def BuildTree(node,list,element): #build a fp-tree
	if(len(list)==0):
		return
	for child in node.children:
		if(child.item==element):
			child.times+=1
		 	del list[0]
			if(len(list)==0):
				return
			BuildTree(child,list,list[0])
			if(len(list)==0):
				return
			break
	new_node=Node()
	node.num_children+=1
	new_node.item=element
	new_node.times+=1
	new_node.parent=node
	node.children.append(new_node)
	del list[0]
	if(len(list)==0):
		return
	BuildTree(new_node,list,list[0])

def Query(tree):#main function of finding common buyers
	temp=raw_input("Please input two items: ")
	a=temp[0]
	b=temp[1]
	for element in sample_list:#swap the sequence of user's input, make it fit the OFI sequence
		if(element==a):
			break
		elif(element==b):
			temp=a
			a=b
			b=temp
			break
	result=0
	A_list=[]
	B_list=[]
	FindA(tree,a,A_list)
	for node in A_list:
		FindB(node,b,B_list)
	for node in B_list:
		result+=node.times
	return result

def FindA(node,a,list):
	if(len(node.children)==0):
		return 
	if(node.item==a):
		list.append(node)
	else:
		for child in node.children:
			FindA(child,a,list)

def FindB(node,b,list):
	if(node.item==b):
		list.append(node)
	else:
		for child in node.children:
			FindB(child,b,list)
		if(len(node.children)==0):
			return

def Draw_tree(node,prefix,isTail):#Draw a tree
	if(isTail):
		temp=prefix+"└── "+node.item
	else:
		temp=prefix+"├── "+node.item
	print temp
	for n in range(0,len(node.children)-1):
		if(isTail):
			Draw_tree(node.children[n],prefix+"    ",False)
		else:
			Draw_tree(node.children[n],prefix+"│   ",False)
	if(len(node.children)>=1):
		if(isTail):
			prefix=prefix+"    "
		else:
			prefix=prefix+"│   "
		Draw_tree(node.children[-1],prefix,True)

file=open('input.txt')
sample_list=[0]*26
temp=0
minimum_support=input("Please input a minimum support: ")
sample_list=stats(file)
print "original sequence is :",
print sample_list

sample_list=swapping(sample_list,minimum_support)
print "after sorting (which meet the minimum_support):",
print sample_list

OFI_list=ordered_frequent_items(file, sample_list)
i=len(OFI_list)
root=Node()
print "Tree Building...... Wait please...."
for n in OFI_list:
	BuildTree(root,n,n[0])
	print OFI_list
print "Your tree has been succefully built, shown as follow:  "
Draw_tree(root,"",True)
result=Query(root)
print result


