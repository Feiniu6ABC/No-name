import sys
c = []
# this will read in every line until the end of file
# caution: the newline at the end of a line is not automatically stripped!
def main():
    b = []
    for line in sys.stdin:
    # if the line was empty (contains only a newline), what does the problem
    # statement ask you to do?
        
        a = []
        line = line.strip()
        if line == "":
            print("")
            continue
        for i in line:
            if i == "X":
                a.append("1")
            else :
                a.append("0")
        a = "".join(a)
        a = int(a,2)
        
        print(chr(a),end="")
    

c = main()
print(c)
    # if the line is not empty, it corresponds
    # to some ascii character - do something with it!
