def differentSubstringsTrie(inputString):
    ss = set()
    for i in range(len(inputString)):
        for j in range(1+i, len(inputString)+1):
            ss.add(inputString[i:j])
            
    return len(ss)
