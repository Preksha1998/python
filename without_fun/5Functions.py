nums = [1,2,3,4,5]
print(nums)
print("num[0] =",nums[0])
print("num[1] =",nums[1])
print("num[2] =",nums[2])
print("num[3] =",nums[3])
print("num[4] =",nums[4])
print("num[0:3] =",nums[0:3])
print("num[2:] =",nums[2:])
print("num[-1] =",nums[-1]) # right to left

names =['prekshu','prerak','viru','mahu','kasish','dhunu']
print("\n\nNames = ",names)

val = [9.5,'prekshu',23]
print("\n\nValues =",val)

comb = [nums,names,val]
print("Combine above 3 = ",comb)

nums.insert(2,10)
print("After Inserting num = ",nums)

nums.remove(10)
print("After Removing num = ",nums)

nums.pop(1)
print("After pop num = ",nums)

nums.pop()
print("After pop without giving index num = ",nums)

del nums[1:]    # delete multiple values
print("After delete Multiple values = ",nums)

nums.extend([70,20,35,15,50])  # add multiple values
print("After Adding multiple values =",nums)

m = min(nums)
print("Minimum = ",m)

max = max(nums)
print("Maximum = ",max)

sum = sum(nums)
print("Sum = ",sum)

nums.sort()
print("After sorting  = ",nums)

