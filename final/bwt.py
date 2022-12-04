import sys
from suffixtest import main as suffixtest


def readFromFile(inputData):
    global fastaSeq
    f = open(inputData, "r")
    sequence = ""
    fasta = 0
    allSequences = []
    seq = []
    last = "*"
    for line in f.readlines():
        if line[0] == ">" or line[0] == ";":
            if last == "*":
                last = line[0]
                fasta += 1
            else:
                if last == ">" or last == ";":
                    last = line[0]
                else:
                    allSequences.append(sequence+"$$")
                    sequence = ""
                    fasta += 1
                    last = line[0]
        else:
            sequence += line.rstrip()
            last = line[0]
    if fasta > 0:
        fastaSeq = 1
        allSequences.append(sequence+"$$")
        return allSequences
    elif fasta == 0:
        seq.append(sequence+'|')
        return seq

def bwt(suffix_arrays):
    sequence = readFromFile(sys.argv[1])
    #print(len(sequence))
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
    # suffarr,_ = suffixtest()
    # print(suffarr)
    # #print(len(suffarr))
    bwt()