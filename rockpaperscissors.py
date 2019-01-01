num_matches = int(input())

def winner(char):
    dictionA= dict([("R","S"),("S","P"),("P","R")])
    if char[0] == char [1]:
        return "Tie"
    for keys in dictionA.keys():
        if keys == char[0] and dictionA[keys]==char[1]:
            return "A"
    return "B"
Alice = 0
Bob = 0
for i in range(num_matches):
    countA = 0
    countB = 0
    match = input().split()
    for i in match:
        if winner(i) == "A":
            countA +=1
        if winner(i) == "B":
            countB +=1
    if countA > countB:
        Alice += 1
    if countA < countB:
        Bob += 1
if Bob > Alice:
    print("Bob",Bob)
else:
    print("Alice", Alice)
   # print("Bob",countB)
    # now you do the rest!
    # read in the rounds in this match
    # example: if the line of input was "RR RP SR" then
    # rounds == ["RR", "RP", "SR"]
    

# print here whoever is the overall winner of all the matches and
# how many matches the winner won
