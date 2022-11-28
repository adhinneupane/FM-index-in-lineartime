'''
Created on Jun 9, 2014

@author: nectarios
'''
import sys
from FileReader import FileReader
from WaveletTree import WaveletTree

def main():
    file_reader = FileReader(sys.argv)
    if (not file_reader.is_read()):
        sys.exit()
    wavelet_tree = WaveletTree(file_reader.get_characters())
    print(wavelet_tree.track_symbol(1))
    print(wavelet_tree.rank_query('p', 35))
    print(wavelet_tree.select_query('e', 3))
    
if __name__ == '__main__':
    main()