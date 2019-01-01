# put your solution heresadf
sf = input()
buses = []
for i in input().split():
    buses.append(int(i))
    #print(buses)
buses = sorted(buses)

def find(List,pos):
    ls =[]
    ls.append(List[pos])
    for i in range(pos,len(List)):
        try:        
            if List[i]+1 == List[i+1]:
                ls.append(List[i+1])
            else:
                break
        except IndexError:
            break
    a = len(ls) -1 
    if len(ls) > 2:
        #print(ls)
        return str(ls[0]) + "-" +str(ls[a]),pos+len(ls)
    #print(ls)
    return str(ls[0]),pos+1
    
b = 0
result = []
while b <= len(buses):
    #result = []
    a,b= find(buses,b)
    result.append(a)
    if b == len(buses):
        break
print(" ".join(result))
        
        