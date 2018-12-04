#Printing Prime Numbers within a certain range

s,e=input("Enter the limits ")
for i in range (s,e+1,1):
	f=0
	for j in range (1,i,1):
        	if i%j==0:
			f+=1
	if(f==1):
		print i

