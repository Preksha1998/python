no = int(input("Enter no of Rows :"))
for i in range(no):
	for j in range(no - i):
		print("* ",end = " ")
	print()