def person1(name,age):
	print("Name = ",name)
	print("Age = ",age + 1)


def person2(name,age = 18):
	print("Name = ",name)
	print("Age = ",age)

def add(a,*b):
	sum = a 
	for i in b:
		sum = sum + i
	print(type(a))
	print(type(b))
	print("Sum = ",sum)

print("1) Position :")
person1("preksha",21)

print("2) Keywords :")
person1(age = 21,name = "preksha")

print("3) Default :")
person2("Preksha") # if you pass age iit will overridde

print("4) variable length :")
add(5,6,7,8,9)