alpha = 0
for i in range(0,5):
	j = i+1
	while(j < 5):
		alpha += j
		j += 1
	alpha += i
print("alpha = ",alpha)

