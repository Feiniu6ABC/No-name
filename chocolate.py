choc,jars = map(int,input().split())
count = 0
for i in range(0,jars):
    stored,cap = map(int,input().split())
    if cap -stored >= choc:
        count += 1
print(count)
    
    