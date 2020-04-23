def sumProblem(x,y):
	sum=x+y
	sentence= "sum of {} and {} is {}.".format(x,y,sum)
	print(sentence)

def main():
	sumProblem(2,3)
	sumProblem(2.3,3.5)
	sumProblem(2,7.2)
	a=int(input("enter first number"))
	b=int(input("enter  second number"))
	sumProblem(a,b)
	x=int(input("enter first number"))
	y=int(input("enter  second number"))
	sumProblem(x,y)
main()