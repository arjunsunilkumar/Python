#counting the consonants, words, question marks, digits and vowels in a string
s=raw_input("Enter a sentence ")
cc=0
cw=1
cq=0
cd=0
cv=0
for i in range(0,len(s),1):
  if (s[i]=="?"):
    cq+=1
  if (s[i].isdigit()!=0):
    cd+=1
  if (s[i]==" "):
    cw+=1
  if(s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u" or s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U"):
    cv+=1
  else:
    cc+=1
cc=1+cc-cw-cd-cq
print "Number of consanants ",cc
print "Number of words ",cw
print "Number of question marks ",cq
print "Number of digits ",cd
print "Number of vowels ",cv


