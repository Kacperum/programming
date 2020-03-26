# Unfinished
def mode(x):

	cdict = []
	wlist = sorted(x)
	mode = {x[0] : wlist.count(wlist[0])}

	for i in x:
		if i not in clist:
			clist.append(i)

	for i in clist:
		if x.count(i) > x.count(mode[0]):
			mode[0] = i

	return(mode)

list1 = [5,6,6,4]
print(mode(list1))
