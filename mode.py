words = input().split()

# words is now a list of all strings in the input
keys = []
diction = {}
def count(char,List):
    count = 0
    for i in range(0,len(List)):
        if char == List[i]:
            count += 1
    return count


def get_key(dic,value):
    result = []
    for i in dic.keys():
        if dic[i] == value:
            result.append(i)
    return result

def max_values(dic):
    a = max(dic.values())
    return a

for i in words:
    if i not in diction.keys():
        diction[i] = count(i,words)
#print(diction)
result = get_key(diction,max_values(diction))
for i in result:
    print(i)
