# read the input
char = input()
List = ["a","e","i","o","u","A","E","I","O","U"]
# solve the problem
count = 0
for i in char:
    if i in List:
        count += 1
# output the result
print(count)