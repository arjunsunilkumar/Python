Basic Calculator 
def addition(a,b):
	addi=a+b
	return addi
def subtraction(a,b):
	subt=a-b
	return subt
def multiply(a,b):
	mult=a*b
	return mult
def divide(a,b):
	divi=a/b
	return divi
def sqrt(a):
	sqrt=a**0.5
	return sqrt
def exponent(a,b):
	expo=a**b
	return expo
print "Menu"
print "1.Addition"
print "2.Subtraction"
print "3.Multiplication"
print "4.Division"
print "5.Exponential"
print "6.Square root"
r=input("Enter the choice ")
t=1
if r==6:
	a=input("Enter the number ")
	result=sqrt(a)
else: 
	a,b=input("Enter the numbers to be operated on ")
	if r==1:
		result=addition(a,b)
	elif r==2:
		result=subtraction(a,b)
	elif r==3:
		result=multiply(a,b)
	elif r==4:
		result=divide(a,b)
	elif r==5:
		result=exponent(a,b)
	else:
		t=0
		print "INVALID OPTION!!"
if(t==1):
	print "Result is ",result
