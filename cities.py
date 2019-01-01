n = int(input())
dic = {}
for i in range(n):
    # now get the two city strings for each of the first n lines
    # Hint: Consider using a dictionary here...
    # replace the pass keyword below with your code
    line = input().split("---")
    dic[line[0]] = line[1]
# you still have to read in the 2nd part of the input
# which consists of the value q followed by the q query lines
q = int(input())
#print(dic) #

def find_route(start, diction):
    count = 0
    while start != "Edmonton":
        start = diction[start]
        count += 1
        #print(start,count)
    return count

List = []
for i in range(q):
    List.append(input())

for i in List:
    a = find_route(i,dic)
    print(a)