#check if a string is a palindrome 
s=raw_input("Enter a sentence ")
for i in range(0,len(s),1):
  if(s[i:i+1:1]==s[len(s)-i-1:len(s)-i:1]):
   continue
  else:
   print"Not Palindrome"
   break
else:
  print "Palindrome"
