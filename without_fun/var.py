num = 12
print("Data Type for num =",type(num))
print("Address of Num = ",id(num))

comp = 18j
print("\nData Type for Complex =",type(comp))
print("Address of Complex",id(comp))

lst = [5,10,15,20]
print("\nData Type for List =",type(lst))

s = {1,4,6,8,2}
print("\nData Type for Set =",type(s))

t = (5,9,1,3,6)
print("\nData Type of Tuple =",type(t))

print("\nRange upto 10 =",range(10))

print("\nList And Range between 1 to 10 :",list(range(10)))

print("\nList odd Numbers btween 1 to 10 :",list(range(2,10,2)))


a = 10
b = a

print("Address of A = ",id(a))
print("Address of B = ",id(b))
