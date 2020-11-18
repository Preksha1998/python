def remove_duplicate_name(n):
	names = []
	for i in range(n):
		print("Enter Name ",i+1)
		names.append(input())

	print("\n\t\t*** After Removing Duplicate Names ***\n")
	s = set(names)
	names = list(s)
	for x in names:
		print(x)

n = int(input("Enter How many Names you want to enter : "))
remove_duplicate_name(n)
#print(result)