import numpy as np 

arr = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])

print("Array = ",arr)
#print(id(arr))
print("ndim(give you number of dimension) = ",arr.ndim)
print("shape(give you no. rows and cols) = ",arr.shape)
print("Address of array = ",id(arr))
print("size(give size of entire block) = ",arr.size)


#convert multidimensional to single dimensional 
arr2 = arr.flatten()
print("1-D Array =",arr2)

#single to multidimensional

arr3 = arr2.reshape(3,4) #3row 4cols -> 3 1-d array with 4 values
print("multidimensional Array =\n ",arr3)

arr4 = arr2.reshape(2,2,3) # 2 2-d Array with 2 1-d array with 3 values
print("multidimensional Array =\n ",arr4)

#a = 10
#print(id(a))