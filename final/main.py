from suffix_array import main as suffix_array
from suffixtest import main as suffix_array_fast
from bwt import bwt
from WaveletTree import WaveletTree
from FMIndex import count
import sys
import time

start_time = time.time()



def readFile(inputData):
    f = open(inputData, "r")
    sequence = ""

    allSequences = []
    seq = []
    last = "*"
    for line in f.readlines():
        sequence = line.rstrip()
        last = line[0]
        seq.append(sequence)
    return seq

if __name__ == '__main__':
    fileData = readFile(sys.argv[1])
    #print(fileData)
    # suffix_arrays, first_indexes = suffix_array()
    suffix_arrays, first_indexes = suffix_array_fast()
    print("Suffix array generated")
    n = len(suffix_arrays)
    bwt_arrays = bwt(suffix_arrays)
    print("BWT generated")
    #print(first_indexes, bwt_arrays)
    wavelet_trees = []
    for i in bwt_arrays:
        wavelet_trees.append(WaveletTree(i))
    for i in range(n):
        end_time = time.time()
        #p = input('Enter search string: ')
        restart_time = time.time()
        print("Count is:" , count("LLA", wavelet_trees[i], first_indexes[i], bwt_arrays[i]))
        final_time = time.time()
        elapsed_time_creation = (end_time - start_time) 
        print('The creation of index took %f seconds to run.' % elapsed_time_creation)
        elapsed_time_query = final_time - restart_time
        print('The query took %f seconds to run.' % elapsed_time_query)
        totalTime = elapsed_time_creation+elapsed_time_query
        print('The total program took %f seconds to run.' % totalTime)




