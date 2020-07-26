a = int(input("Enter Number 1 :"))
b = int(input("Enter Number 2 :"))

print("\n \t\t*** Before Swapping ***")
print("\tA = ",a)
print("\tB = ",b)

a = a + b 
b = a - b
a = a - b

print("\n \t\t*** After Swapping with Operator ***")
print("\tA = ",a)
print("\tB = ",b)

x = 10
y = 20

print("\n \t\t*** Before Swapping ***")
print("\tX = ",x)
print("\tY = ",y)

print("\n \t\t*** After Swapping with XOR ***")

x = x ^ y 
y = x ^ y
x = x ^ y


print("\tX = ",x)
print("\tY = ",y)

p = 50
k = 100

print("\n \t\t*** Before Swapping ***")
print("\tP = ",p)
print("\tK = ",k)


print("\n\t\t *** After Swapping with 1 Line")

p,k = k,p

print("\tP = ",p)
print("\tK = ",k)

