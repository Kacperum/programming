def fibonacci(x):

	fibonacci = [0,1]
	a = 0
	b = 1

	for i in range(x - 2):

		if a > b:
			b += a
			fibonacci.append(b)

		elif a <= b:
			a += b
			fibonacci.append(a)

	return(fibonacci[x - 1])
