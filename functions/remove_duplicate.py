def remove_duplicate(str1):
	new_str = []
	for i in str1:
		if i not in new_str:
			new_str.append(i)
	return new_str		

#str1 = [1,4,2,1,5]
str1 = []
n = int(input("How many element you want in list :"))
for i in range(0,n):
	element = input()
	str1.append(element)
print(" List = " + str(str1))

print("New List =",remove_duplicate(str1))