# Finds the factorial of the inputted number.

factorial = int(input("Factorial:"))
answer = 1

for i in range(1,factorial + 1):

	answer *= i

print(factorial,"! = ",answer)
