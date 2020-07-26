def factorial(n):
	fact = 1
	if n < 0 :
		print("Number should be greater than 0..")
	elif n == 0 :
		print("Factorial of 0 is 1..")
	else:
		for i in range(1,n + 1):
			fact = fact * i
			i = i + 1
		print("Factorial is",fact)

n = int(input("enter number : "))
factorial(n)
