#k = 2 * 5 - 2
k = 2 * 5 - 2
for i in range(5):
	for j in range(k):
		print(end = " ")
	k = k - 2
	for j in range(0,i + 1):
		print("*  ",end = " ")
	print()
	
for i in range(5):
	for j in range(5 - i):
		print("*  ",end = " ")
	print()

	for j in range(i + 1):
		print(" ",end = " ")