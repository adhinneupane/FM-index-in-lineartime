from itertools import zip_longest, islice
import sys
from collections import defaultdict
import pickle


def sort_bucket(s, bucket, order):
    d = defaultdict(list)
    for i in bucket:
        key = s[i + order // 2:i + order]
        d[key].append(i)
    result = []
    for k, v in sorted(d.items()):
        if len(v) > 1:
            result += sort_bucket(s, v, 2 * order)
        else:
            result.append(v[0])
    return result


def suffix_array_ManberMyers(s):
    return sort_bucket(s, range(len(s)), 1)

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

def to_int_keys_best(l):
    """
    l: iterable of keys
    returns: a list with integer keys
    """
    seen = set()
    ls = []
    for e in l:
        if not e in seen:
            ls.append(e)
            seen.add(e)
    ls.sort()
    index = {v: i for i, v in enumerate(ls)}
    return [index[v] for v in l]


def suffix_matrix_best(s):
    """
    suffix matrix of s
    O(n * log(n)^2)
    """
    n = len(s)
    k = 1
    line = to_int_keys_best(s)
    ans = [line]
    while max(line) < n - 1:
        line = to_int_keys_best(
            [a * (n + 1) + b + 1
             for (a, b) in
             zip_longest(line, islice(line, k, None),
                         fillvalue=-1)])
        ans.append(line)
        k <<= 1
    return ans


def suffix_array_best(s):
    """
    suffix array of s
    O(n * log(n)^2)
    """
    n = len(s)
    k = 1
    line = to_int_keys_best(s)
    while max(line) < n - 1:
        line = to_int_keys_best(
            [a * (n + 1) + b + 1
             for (a, b) in
             zip_longest(line, islice(line, k, None),
                         fillvalue=-1)])
        k <<= 1
    return line

def inverse_array(l):
    n = len(l)
    ans = [0] * n
    for i in range(n):
        ans[l[i]] = i
    return ans

def writetoFile(outSuffixArray,fIA):
    with open('outarray'+sys.argv[1]+'.pkl', 'wb') as f:
        pickle.dump(outSuffixArray,f)
    with open('fia'+sys.argv[1]+'.pkl', 'wb') as f:
        pickle.dump(fIA,f)

def readfromPickle():
    with open('outarray'+sys.argv[1]+'.pkl', 'rb') as f:
        o = pickle.load(f)
    with open('fia'+sys.argv[1]+'.pkl', 'rb') as f:
        fi = pickle.load(f)
    return o,fi
    


def main():
    sequence = readFromFile(sys.argv[1])
    p = input("load array from pickle?: (Y/n)")
    if p == 'n':
        outputSuffixArray =inverse_array(suffix_array_best(sequence[0]))
        firstIndexArray = [sequence[0][i] for i in outputSuffixArray]
        writetoFile(outputSuffixArray,firstIndexArray)
    else:
        outputSuffixArray, firstIndexArray = readfromPickle()
    #print([outputSuffixArray], [firstIndexArray])
    return [outputSuffixArray], [firstIndexArray]



if __name__ == "__main__":
    main()