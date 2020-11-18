import os.path, time
print(__file__,"\nCreation time:",time.ctime(os.path.getatime(__file__)))
num="0123456789"
alpha="ABCDEFGHIJKLMNPQRSTUVWXYZ"
for i in num:
	for j in alpha:
		for k in alpha:
			for l in num:
				for m in num:
					for n in num:
						print("GJ 01 ",j,k,i,l,m,n)
