while True:
	print("OPTIONS:")
	print("Enter 1 to Add.")
	print("Enter 2 to Subtract.")
	print("Enter 3 to Multiply.")
	print("Enter 4 to Divide.")
	ch=int(input("Enter Your Choice:"))
	n1=float(input("Enter First Number:"))
	n2=float(input("Enter Second Number"))
	if ch==1:
		print(n1+n2)
	elif ch==2:
		if n1>n2:
			print(n1-n2)
		else:
			print(n2-n1)
	elif ch==3:
		print(n1*n2)
	elif ch==4:
		if n2==0:
			print("Maths Error.")
		else:
			print(n1/n2)
	else:
		print("Wrong Input.")
	a=input("More Calculations?(Y/N)")
	if a=='Y':
		continue
	else:
		break
	