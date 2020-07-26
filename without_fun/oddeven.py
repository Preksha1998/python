# odd even
no = int(input("Enter Number to Check wether the odd or even :"))
rem = no % 2

if rem == 0:
	print(no," is odd.")
else:
	print(no," is even.")