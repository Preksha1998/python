lst = []

n = int(input("Enter how many element you want to Enter :"))

for i in range(n):
	ele = int(input())
	lst.append(ele)

print(lst)

odd_num = [num for num in lst if num % 2 == 1]
print("Odd Number using list comprehension = ",odd_num)

odd_num2 = list(filter(lambda x:(x % 2 != 0),lst))
print("Odd Number usin lambda expression =",odd_num2)