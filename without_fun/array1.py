from array import *
ch = 1
while ch != 0:
	print("1. Without function search Element..")
	print("2. with function search Element..")
	print("0. Exit..")
	
	ch = int(input("Enter Choice :"))

	if ch == 1 :
		arr = array('i',[])

		n = int(input("Enter How Many Elements you want :"))

		for i in range(n):
			x = int(input("Enter Element : "))
			arr.append(x)

		for i in range(n):
			print(arr[i])

		sval = int(input("Enter Search Element :"))

		k = 0
		for e in arr:
			print(e)
			if e == sval:
				print("search value is found at position ",k)
				break
			k = k + 1
	if ch == 2:
		
		arr = array('i',[])

		n = int(input("Enter How Many Elements you want :"))

		for i in range(n):
			x = int(input("Enter Element : "))
			arr.append(x)

		for i in range(n):
			print(arr[i])

		sval = int(input("Enter Search Element :"))
		print("Element is found at psition : ")
		print(arr.index(sval))
	if ch == 0:

		exit(0)