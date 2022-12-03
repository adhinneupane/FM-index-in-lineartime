import sys

def bwt(suffix_arrays):
    sequence = list(open(sys.argv[1], "r"))
    bwt = []
    for i in range(len(suffix_arrays)):
        s = suffix_arrays[i]
        
        temp = []
        for j in s:
            #print(sequence)
            temp.append(sequence[i][j-1])
        bwt.append(temp)
    
    return bwt

if __name__ == "__main__":
    bwt()