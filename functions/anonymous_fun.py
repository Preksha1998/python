from functools import reduce
def add_all(a,b):
	return a + b


nums = [3,5,2,7,8,1,9,4]

evens = list(filter(lambda n : n%2 == 0,nums))#gives even no from nums list
print(evens)

double = list(map(lambda n : n*2,evens))# give square no for even no from evens
print(double)

sum = reduce(add_all,double)#sum of double numbers / 
							 #insted of add_all fun you can use lambda like lambda a,b : a+b
print(sum)