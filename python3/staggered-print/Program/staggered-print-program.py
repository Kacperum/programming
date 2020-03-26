word	= input("Word: ")
maxi	= int(input("Max stagger: "))
stagger	= 0

for i in word:
	
	print(stagger * " ",i)
	stagger += 1
	
	if stagger == maxi:
		stagger = 0 
