r = int(input("Enter Number of Rows :"))
c = int(input("Enter Number of cols :"))

print("Take Inputs :")

matrix = []
for i in range(r):
	a = []
	for j in range(c):
		a.append(int(input()))
	matrix.append(a)

print("\n*** MATRIX ***\n")
for i in range(r):
	for j in range(c):
		#print("{:>10} {:>10}". format (i,j))
		print("{:<10}".format(matrix[i][j])," ",end = " ")
	print()

	
