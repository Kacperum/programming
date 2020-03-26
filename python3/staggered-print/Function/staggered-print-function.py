def staggered_print(word,maxi):

	stagger = 0

	for i in word:

		print(stagger * " ",i)
		stagger += 1

		if stagger == maxi:
			stagger = 0
