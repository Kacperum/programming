def median(x):

	x.sort()

	if len(x)%2 == 1:

		return(x[int((len(x)-1)/2)])

	else:

		return((x[int(len(x)/2)]+x[int(len(x)/2-1)])/2)
