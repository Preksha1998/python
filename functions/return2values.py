def add_sub(x,y):
    s = x + y
    d = x - y
    return s,d

a =int(input("enter value 1 ="))
b =int(input("enter value 2 ="))
result1,result2 = add_sub(a,b)
print("addition = ",result1,"\nsubtraction = ",result2)