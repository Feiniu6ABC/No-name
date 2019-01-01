# Read in the input
elements = int(input())
diction = {}
for i in range(0,elements):
    ls = input().split()
    diction[ls[0]] = ls[1]
#print(diction)
# Construct a dictionary mapping binary strings to English words
text = []
for i in input():
    text.append(i)


def find(text,pos,diction):
    str1 = [] 
    for i in text[pos:]: ##may wrong
        a = "".join(str1)
        if a not in diction.keys():
            str1.append(i)
        else:
            break
    a = "".join(str1)
    return diction[a],pos+len(str1)


pos = 0
result = []

while pos<len(text):
    word,pos=find(text,pos,diction)
    result.append(word)
print(" ".join(result))
# Use the dictionary to decode the binary string
