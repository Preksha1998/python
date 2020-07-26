def addition(x,y):
    add = x + y
    return add

def subtraction(c,d):
	sub = c - d
	return sub

def multiplication(e,f):
	mul = e * f
	return mul

def division(g,h):
	div = g / h
	return div
   
a = int(input("enter value :")) 
b = int(input("enter value :"))

ch = 1
while ch != 0 :
	print("\n1.Addition..")
	print("\n2.Subtraction..")
	print("\n3.Multipliation..")
	print("\n4.Division..")
	print("\n0.exit..")

	ch = int(input("enter your choice :"))

	if (ch == 1):
		result = addition(a,b)
		print("\nAddition =",result)

	elif (ch == 2):
		result = subtraction(a,b)
		print("\nSubtraction =",result)

	elif (ch == 3):
		result = multiplication(a,b)
		print("\nMultiplication = ",result)

	elif (ch == 4):
		result = division(a,b)
		print("\nDivision = ",result)

	else :
		print("\nenter correct choice..")