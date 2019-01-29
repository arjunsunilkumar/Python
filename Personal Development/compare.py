f1 = open("/Users/rset/Desktop/keywordsc.txt", 'r')
f2 = open("/Users/rset/Desktop/keywordspy.txt", 'r')
output = open("/Users/rset/Desktop/keywordscom.txt", 'w')
words1 = f1.read().split()
words2 = f2.read().split()
words = set(words1) & set(words2)
for word in words:
        output.write(word)
