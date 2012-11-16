class Fork:		
	def __init__(self, chars, weight, left=None, right=None):
		self.chars=chars
		self.weight=weight
		
		self.left=left
		self.right=right

			
def encode(string,tree):
	return encodeHelper(string,tree,tree,"")
	
def encodeHelper(a,node,tree,st):
	if a=='':
		return st
	elif node.left==None:
		return encodeHelper(a[1:],tree,tree,st)
	elif a[0] in node.left.chars:
		return encodeHelper(a,node.left,tree,st+'0')
	else:
		return encodeHelper(a,node.right,tree,st+'1')
	
			
def decode(string,tree):
	return(decodeHelper(string,tree,tree,""))

def decodeHelper(a,node,tree,st):
	if a=="":
		return(st+node.chars)
	elif node.left==None:
		return(decodeHelper(a,tree,tree,st+node.chars))
	elif a[0]=='0':
		return(decodeHelper(a[1:],node.left,tree,st))
	else:	
		return(decodeHelper(a[1:],node.right,tree,st))
	
	

def makeCodeTree(codestring):
	nodes=sorted([Fork(i,j) for (i,j) in count(codestring).items()],key=lambda x:x.weight)
	while len(nodes) > 1:
		nodes=sorted(([Fork(nodes[0].chars+nodes[1].chars,nodes[0].weight+nodes[1].weight,nodes[0],nodes[1])]+nodes[2:]),key=lambda x:x.weight)
	return(nodes[0])
	
def count(a):
	cnt={}
	for i in a :
		if i in cnt:
			cnt[i]=cnt[i]+1
		else:
			cnt[i]=1

	return(cnt)

	
		
		
def makecodList(codeTree):	
	codList=makecodListNew(codeTree)
	codListNew={}
	for (i,j) in codList:
		codListNew[i]=j
	return(codListNew)

def makecodListNew(tree):
	if tree.left == None :
		return [(tree.chars,'')]
	rightTable=makecodListNew(tree.right)
	leftTable=makecodListNew(tree.left)
	return [(i,'0'+j) for (i,j) in leftTable]+[(i,'1'+j) for (i,j) in rightTable]		
	
	
	
def quickEncode(string,codList):
	st=""
	for i in string:
		st=st+codList[i]
	return st
		
def test():
	print 'tree for the string "zxcvbnmlkjhgfdsaqwertyuiop" created'
	tree=makeCodeTree("zxcvbnmlkjhgfdsaqwertyuiop")
	table=makecodList(tree)
	print "code table:" ,table
	print 'string: "lkjh" code: ', encode("lkjh",tree)
	print 'code: "0110011110110000111" string: ', decode("0110011110110000111",tree)
test()
	
