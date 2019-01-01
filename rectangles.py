# Read in the input
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# Solve the problem
X = [x1,x2,x3]
Y = [y1,y2,y3]

# Output the result
def f_distin(List,Int):
    count = 0
    for i in List:
        if i == Int:
            count +=1
        if count > 1:
            return 
    return Int
for i in X:
    if (f_distin(X,i) == i):
        x = f_distin(X,i)
        
for i in Y:
    if (f_distin(Y,i) == i):
        y = f_distin(Y,i)

print(x, y)
    
        
        
        
                
