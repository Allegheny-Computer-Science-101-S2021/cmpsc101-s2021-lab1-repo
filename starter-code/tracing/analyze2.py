beta = 0
for i in range(0,3):
	for j in range(3,6):
		while(j > i):
			beta += j - i
			j -= 1	
	beta += i + j
print("beta = ",beta)

