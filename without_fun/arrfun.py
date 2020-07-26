lst = []

n = int(input("Enter How Many Elements :"))

for i in range(n):
	ele = str(input("Enter Name :"))
	lst.append(ele)

print("\n")
x = lst.count("rr")
print(x)

print("\n")
for i in range(n):
	print("Name = ",lst[i])

r = str(input("\nwhich Name you want to  remove :"))
lst.remove(r)
print("\nAfter removing Elemenet List")
for i in range(n - 1):
	print(lst[i])



p = int(input("\nwhich index name you want to pop :"))
lst.pop(p)
print("\nAfter pop Elemenet List")
print(lst)


cpy = lst.copy()
print("\nCopied Lists")

for i in range(n - 2):
	print(cpy[i])

print("\n")
print("extend another list\n")
ex = ['xx','yy','zz']
lst.extend(ex)
print(lst)

print("\nreverse list\n")

lst.reverse()
print(lst)

print("\nsort arry\n")
lst.sort()
print(lst)