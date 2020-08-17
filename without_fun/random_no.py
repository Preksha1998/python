import random
n = random.randint(1,30)
print("Random Number :",n)


randomlst = random.sample(range(0,30),5)
print("Elements List :",randomlst)


randomlst2 = []
for i in range(0,5):
	n = random.randint(1,30)
	randomlst2.append(n)
	print(randomlst2)


randomlst3 =[random.randrange(50)for i in range(7)]
print("Random Number List = ",str(randomlst3))