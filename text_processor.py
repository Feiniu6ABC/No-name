def rm_syb(char,List):
    b = []
    for i in char:
        if i not in List:
            b.append(i)
    b ="".join(b)
    return b 
def is_numbers(char):
    count = 0
    for i in char:
        if ord("0") <= ord(i) and ord(i)<=ord("9"):
            count += 1
    if count == len(char):
        return True
    else:
        return False
def text_process(char):
    a = []
    stp = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", 
    "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", 
    "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", 
    "themselves", "what", "which","who", "whom", "this", "that", "these", "those", 
    "am", "is", "are", "was", "were", "be","been", "being", "have", "has", "had", 
    "having", "do", "does", "did", "doing", "a", "an","the", "and", "but", "if", 
    "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", 
    "about", "against", "between", "into", "through", "during", "before", "after", 
    "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over",
    "under", "again", "further", "then", "once", "here", "there", "when", "where", 
    "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", 
    "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", 
    "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]    
    processed = []
    for i in range(32,97) or range(98,127):
        a.append(chr(i))
    char = char.lower()
    char = char.split()
    for i in char:
        if is_numbers(i) == False:
            if rm_syb(i,a) not in stp:
                processed.append(rm_syb(i,a))
        if is_numbers(i) == True:
            processed.append(i)
    return processed
    
if __name__ == "__main__":
    processed = text_process(input("Input: "))
    print(processed)
                 