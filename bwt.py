import sys

def writeToFile(allArray, outputData):
    f = open(outputData, "w")
    for array in allArray:
        for item in array:
            f.write(item+" ")
        f.write("\n")

def bwt():
    sequence = list(open(sys.argv[1], "r"))
    suffix_arrays = list(open(sys.argv[2], "r"))

    bwt = []
    for i in range(len(suffix_arrays)):
        s = suffix_arrays[i].split(" ")
        s.pop()
        
        temp = ""

        for j in s:
            temp += sequence[i][int(j)-1]
        bwt.append(temp)
    writeToFile(bwt, sys.argv[3])

if __name__ == "__main__":
    if len(sys.argv) != 4:
        # if incorrect number of command line parameters, error
        print("Incorrect number of parameters.")
    else:
        bwt()
