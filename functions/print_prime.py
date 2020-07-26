def print_prime(min_no,max_no):
		for num in range(min_no,max_no + 1):
			if num > 1:
				for i in range(2,num):
					if (num % i == 0):
						break
				else:
					print(num)

min_no = int(input("Enter lower Number:"))
max_no = int(input("Enter upper Number:"))

print_prime(min_no,max_no)