def evenodd(num):
	if(num%2==0):
		return 0;
	else:
		return 1;
	
num=int(input("enter number"))
z=evenodd(num)
if(z==0):
	print("number is even")
else:
	print("odd")