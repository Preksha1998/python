import random
r = int(input("Enter Number of Rows :"))
c = int(input("Enter Number of cols :"))

matrix = []
for i in range(r):
	a =[]
	for j in range(c):
		n = random.randint(1,100)
		a.append(n)
	matrix.append(a)

print("\n *** Matrix *** \n")
for i in range(r):
	for j in range(c):
		print("{:>10}".format(matrix[i][j])," ",end = " ")
	print()

print("\n*** ODD_EVEN MATRIX ***\n")	
for i in range(r):
	for j in range(c):
		if j % 2 == 0:
			print("-{:<10}".format(matrix[i][j])," ",end = " ")
		else:
			print("{:<10}".format(matrix[i][j])," ",end = " ")
	print()