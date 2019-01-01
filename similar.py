# Read in the input
a,b,c = map(int, input().split())

# Solve the problem and output the result
count = 0
if a==b:
    count+=1
if a == c:
    count += 1
if b == c:
    count += 1
if count == 0:
    print("distinct")
if count == 1:
    print("similar")
if count == 3:
    print("same")