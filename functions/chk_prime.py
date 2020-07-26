def chk_prime(n):
	if n <= 1:
		return False
	else:

		for i in range(2,n):
			if(n % i == 0):
				return False
		return True

no = int(input("enter number : "))
if chk_prime(no):
	print(no," is a prime..")
else :
	print(no," is not prime..")