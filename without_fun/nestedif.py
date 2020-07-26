no = int(input("Enter number : "))

if no % 2 == 0:
	if no % 3 == 0:
		print(no," is divisible by 2 and 3.")
	else:
		print(no," is divisible by 2 only..")
elif no % 3 == 0:
	print(no," is divisible by only 3.")
else:
	print(no," is not divisible by 2 or 3..")