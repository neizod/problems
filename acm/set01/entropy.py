class Tree:
	'''since python doen't implement tree, implement it!'''
	def __init__(self, n=0, l=None, r=None):
		self.n = n	# node's value
		self.l = l	# leftside
		self.r = r	# rightside

def push(pop1, pop2):
	'''make sub-tree which has pop values as left-right node, then push in and sort the tque'''
	global tque
	new = Tree(pop1.n + pop2.n, pop1, pop2)

	ins = False
	for i in range(len(tque)):
		if tque[i].n >= new.n:
			tque.insert(i, new)
			ins = True
			break
	if not ins:
		tque.append(new)

def pop(que):
	'''just ordinary pop function, for shorten code'''
	out = que[0]
	del que[0]
	return out

def poplt():
	'''pop either lque or tque which has minimum value, return None when both are empty'''
	global lque, tque

	if len(lque) == 0 and len(tque) == 0:
		return None
	if len(lque) == 0:
		return pop(tque)
	elif len(tque) == 0:
		return pop(lque)
	else:
		if lque[0].n <= tque[0].n:
			return pop(lque)
		else:
			return pop(tque)

def get(node, d=0):
	''' get the value of node's path multiplication by its times occurent'''
	global sumtable
	if node.l == None and node.r == None:
		sumtable.append(node.n*d)
	if node.l != None:
		get(node.l, d+1)
	if node.r != None:
		get(node.r, d+1)

################################################################################

import re

while True:
	raw = input()
	raw = re.sub('\r|\n', '', raw)
	if raw == 'END':
		break

	## get frequency of each alphabet then sort from minimum to maximum to list-deque##
	dict = {}
	for c in raw:
		if c not in dict:
			dict[c] = 1
		else:
			dict[c] += 1
	lque = sorted(dict.values())

	## create sub-tree for each sorted value ##
	for i in range(len(lque)):
		lque[i] = Tree(lque[i])

	## create tree-deque for collecting each sub-tree ##
	tque = []

	## Huffman algorithm ##
	while True:
		pop1 = poplt()
		pop2 = poplt()
		if pop2 == None:
			break
		push(pop1, pop2)
	root = pop1

	## recursive get every leaf's path multiplication by its time occurent ##
	sumtable = []
	get(root)

	## print out the answer. hooray! ##
	a = 8*root.n
	b = sum(sumtable)
	print("{0} {1} {2:.1f}".format(a, b, a/b))