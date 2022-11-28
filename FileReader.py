'''
Created on Jun 9, 2014

@author: nectarios
'''
import sys

class FileReader(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        self.character = []
        if len(params) < 2:
            print("Please give correct arguments")
            sys.exit()
        self.__read_file(params[1])
    #Read the txt file and create a list from character
    def __read_file(self,filename=None):
        if filename == None:
            return
        try:
            with open(filename) as f:
                while True:
                    c = f.read(1)
                    if not c:
                        print("Read %i character Successfully" % len(self.character))
                        break
                    if ord(c) == 10:
                        continue                    
                    self.character.append(str(c))
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            raise
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def get_characters(self):
        if len(self.character) == 0:
            return None
        return self.character

    def is_read(self):
        if len(self.character) == 0:
            return False
        return True

if __name__ == '__main__':
    file_reader = FileReader(sys.argv)

        