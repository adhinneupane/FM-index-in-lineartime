

from Node import Node

class WaveletTree(object):
    
    def __init__(self, data=None):
        if data == None:
            print("Please give correct parameters")            
            return
        self.__root = Node(data)  #Create the parent node
        
    """
    Query Functions
    """    
    def rank_query(self,character=None, position=None):
        if character==None or position==None or position < 0:
            print("Please give correct parameters")
            return -1
        return self.__root.get_rank_query(position,character)
    
    def select_query(self,character=None, position=None):
        if character==None or position==None or position <= 0:
            print("Please give correct parameters")
            return -1
        return self.__root.get_select_query(position, character)
    
    def track_symbol(self,position=None):
        if position==None or position <= 0:
            print("Please give correct parameters")
            return -1
        return self.__root.get_track_symbol(position) 
    """
    Query Functions
    """   
