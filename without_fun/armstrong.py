no = int(input("Enter Number :"))

cno = no
sum = 0

while cno > 0 :
	rem = cno % 10
	sum = sum + rem ** 3
	cno = cno // 10

if no == sum :
	print(no," is an Armstrong Number") 
else :
	print(no," is not an Armstrong Number")
