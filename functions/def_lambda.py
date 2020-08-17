def myfun(n):
	return lambda a : a * n

a = int(input("Enter Number :"))
n = int(input("Enter Number :"))

myfun2 = myfun(a)
myfun3 = myfun(3)

print(myfun2(n))

print(myfun3(n))