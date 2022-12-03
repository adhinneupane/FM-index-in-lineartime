from suffix_array import main as suffix_array
from bwt import bwt
from WaveletTree import WaveletTree
from FMIndex import count

if __name__ == '__main__':
    suffix_arrays, first_indexes = suffix_array()
    n = len(suffix_arrays)
    bwt_arrays = bwt(suffix_arrays)
    #print(first_indexes, bwt_arrays)
    wavelet_trees = []
    for i in bwt_arrays:
        wavelet_trees.append(WaveletTree(i))
    for i in range(n):
        p = input('Enter search string')
        print(count(p, wavelet_trees[i], first_indexes[i], bwt_arrays[i]))
