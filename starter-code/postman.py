print("Welcome to the Postman App program ....\n" + "-------------------------------------------------")
while (True):
	left,right = "",""
	first = input("Enter the first house no on your list of delivery:")
	last = input("Enter the last house no on your list of delivery: ")
	# add your logic here to store the result in left, right variables
	# ... 

	# end you logic here
	print("Houses on the left: ("+left+")")
	print("Houses on the right:("+right+")")
	prompt = input("Do you want to continue? (y/n):")
	if (prompt == 'n'):
		break
	else:
		continue
