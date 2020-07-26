from array import *
arr = array('i',[])

n = int(input("Enter How many Elements you want : "))

for i in range(n):
	no = int(input("Enter Number :"))
	arr.append(no)

print("\n")
for i in range(n):
	print("Number = ",arr[i])

max = arr[0]

for i in range(n):
	if max < arr[i]:
		max = arr[i]
print("\n\nMAX = ",max)
