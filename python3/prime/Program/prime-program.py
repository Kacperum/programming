primes = [2]
amount = int(input("Whick prime number do you want?\n"))
num = 1

while len(primes) < amount:

	num += 2
	
	for i in primes:
		rest = 0
		rest += num % i
		if rest == 0:
			break

	if rest != 0:
		primes.append(num)

print("Prime number",amount,"is:\n",primes[amount - 1])
