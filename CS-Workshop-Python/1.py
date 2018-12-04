#Printing number pattern
#10 9 8 7
#6 5 4
#3 2
#1


i=10
p=4
while i>0:
    for j in range(p+1,1,-1):
        print i," ",
        i-=1
    p-=1
    print " "
