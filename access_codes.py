def answer(x):
	num = 0
	solutions = {}
	for char in x:
		reverse = char[::-1]
		if (not(solutions.has_key(reverse) or solutions.has_key(char))):
			solutions[char] = 1;
			solutions[reverse] = 1;
			num += 1
	return num
