def compound_intrst(principal,rate,time):
	amount = principal * (pow((1 + rate / 100),time))
	ci = amount - principal
	return ci

principal = int(input("Enter Value for primcipal : "))
rate = float(input("Enter Value for rate : "))
time = int(input("Enter time : "))

amt = compound_intrst(principal,rate,time)
print("Amount = ",amt)