# The functions find the factorial of x.

def factorial1(x):

	answer = 1

	for i in range(1,x+1):

		answer *= i

	return(answer)



def factorial2(x):

	if x == 1:
		return(1)

	if x > 1:
		answer = x*factorial(x-1)
		return(answer)
