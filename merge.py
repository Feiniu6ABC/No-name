# Get the input
List1 = input().split()
List2 = input().split()
List = []
# Solve the problem
count1 = 0
count2 = 0
a = len(List1)+len(List2)
while True:
    if (count1==count2 and count1<len(List1)) and count1 <  len(List1) or count2 == len(List2) and count1 < len(List1):
        List.append(List1[count1])
        count1+=1
        #print("count1",count1)
    if count2 < count1 and count2<len(List2) and count2 < len(List2) or count1 == len(List1) and count2 < len(List2):
        List.append(List2[count2])
        count2+=1
        #print("count2",count2)
    if len(List) == a :
        break
    #print(List)
# Print the
print(" ".join(List))