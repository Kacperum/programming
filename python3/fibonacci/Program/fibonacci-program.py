fibonacci = [0,1]
amount = int(input("Which Fibonacci number do you want?\n"))
a = 0
b = 1

for i in range(amount - 2):

	if a > b:
		b += a
		fibonacci.append(b)

	elif a <= b:
		a += b
		fibonacci.append(a)

print("Fibonacci number number",amount,"is",fibonacci[amount - 1])
