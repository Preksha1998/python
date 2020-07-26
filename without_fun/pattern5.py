n = int(input("Enter Rows :"))
for i in range (n) :
     for j in range ((n - i + 1) * 2) :
             print (end = " ")
     for k in range (i + 1) :
             print ("*", end = " ")
     print ()



     