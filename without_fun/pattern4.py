k = 2 * 5 - 2
for i in range(5):
	for j in range(k):
		print(end = " ")
	k = k - 2
	for j in range(0,i + 1):
		print("*  ",end = " ")
	print()