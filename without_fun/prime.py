ch = 1
while ch != 0:
	print("1. Check Prime or Not..")
	print("0.Exit..\n")
	ch = int(input("Enter Choice : "))

	if ch == 1:
		num = int(input("Enter Number :"))

		for i in range(2,num):
			if num % i == 0:
				print(num,"is not Prime Number.\n\n")
				break
		else:
			print(num,"is Prime Number.\n\n")
			
	elif ch == 0:
		exit(0)