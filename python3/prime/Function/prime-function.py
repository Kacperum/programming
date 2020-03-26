def prime(x):

	primes = [2]
	num = 1

	while len(primes) < x:
		num += 2

		for i in primes:
			rest = 0
			rest += num % i
			if rest == 0:
				break

		if rest != 0:
			primes.append(num)

	return(primes[x - 1])
