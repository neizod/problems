def refill(lf_c, lf_h, lf_v, path=''):
	global answer
	if answer:
		return
	if lf_c == 0 and lf_h == 0 and lf_v == 0:
		if chk(path):
			answer = True
			print(count(path))
		return
	if lf_c > 0:
		refill(lf_c-1, lf_h, lf_v, path + 'c')
	if lf_h > 0:
		refill(lf_c, lf_h-1, lf_v, path + 'h')
	if lf_v > 0:
		refill(lf_c, lf_h, lf_v-1, path + 'v')

def walk(n):
	for i in range(n+1):
		refill(n-i, i, i)

def chk(path):
	x, y = 0, 0
	for ew in path:
		if xmap[y][x] != '':
			for ec in xmap[y][x]:
				if ec == ew:
					return False
		if ew == 'c':
			x += 1
			y += 1
		if ew == 'h':
			x += 1
		if ew == 'v':
			y += 1
	return True

def count(path):
	l = 0
	for ec in path:
		if ec == 'c':
			l += 1 
		else:
			l += 1
	return l

################################################################################

while True:
	size = int(input())
	if size == 0:
		break

	xmap = [['' for j in range(size+1)] for i in range(size+1)]
	for j in range(size):
		inrow = input()
		for i in range(size):
			if inrow[i] == '#':
				xmap[j][i] += 'c'
				if j > 0:
					if xmap[j-1][i] != '':
						xmap[j][i] += 'h'
				if i > 0:
					if xmap[j][i-1] != '':
						xmap[j][i] += 'v'

	answer = False
	walk(size)
