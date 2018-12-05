#printing a pattern
#1
#2 3
#4 5 6
#7 8 9 10
p=1
i=1
while(i<11):
  for j in range(0,p,1):
    print i,
    i+=1
  print " " 
  p+=1
