

BLOCKS_NUM = 30
BITS_NUM = 50
SUPER_BLOCK_SIZE = 30

class Node(object):
    '''
    classdocs
    '''
    
    def __init__(self, data=None, parent=None, from_left_parent=None):
        '''
        Constructor
        '''
        if data == None:
            print("Please give correct parameters")
            return
        self.full_data = data
        self.data = list(set(data))
        self.data.sort(key=None, reverse=False)
        self.bits_data = []
        self.bits_full_data = []
        self.childern = []
        self.parent = parent
        self.from_left_parent = from_left_parent
        self.rs = []
        self.rb = []
        self.__decode_data()
        self.__create_RRR()
        if self.__size() == 1:
            return
        self.__gen_tree()
    """
    Query Functions
    """   
        
    def get_rank_query(self,position=None, character=None):
        if self.__full_size() < position:
            return -1
        bit = self.__get_bit(character)
        position_size = self.__get_rank(position, bit)   #Calculate the rank
        if self.__size() == 2:                           #When the size is 2 then i find leaf and must finish
            return position_size
        if bit:                                          #For true(1) go to the right child, for false(0) go to the left child
            return self.childern[1].get_rank_query(position_size,character) 
        return self.childern[0].get_rank_query(position_size,character)
    
    def get_select_query(self,position=None, character=None):
        leaf = self.__get_leaf(character)                   #Get the leaf where the character is
        return leaf.__get_select(position,leaf.bits_data[leaf.data.index(character)])

    def get_track_symbol(self,position=None):
        if self.__size() == 2:                           #When the size is 2 then i find leaf and must finish
            return self.full_data[position-1]
        if self.__full_size() < position:
            return -1
        bit = self.bits_full_data[position-1]
        position_size = self.__get_rank(position, bit)   #Calculate the rank
        
        if bit:                                          #For true(1) go to the right child, for false(0) go to the left child
            return self.childern[1].get_track_symbol(position_size)
        return self.childern[0].get_track_symbol(position_size)
    """
    Query Functions
    """   
    """
    Private Functions
    """           
    
    def __get_select(self,position=None,bit=None):
        curent_position = self.__find_position(position, bit)   #Find how many bit has the word until the position
        if self.parent == None:                                 #If is parent then find the position
            return curent_position
        if self.from_left_parent:                               #For left child calculate False(0), for right child calculate True(1)
            return self.parent.__get_select(curent_position, False)
        return self.parent.__get_select(curent_position, True)

    def __find_position(self,position=None, bit=None):
        #position_size = self.__get_rank(position, bit)
        #curent_position = position#self.__get_rank(position, bit)                
        #position_size = curent_position
        #if position_size == position:
        #    return curent_position
        position_size = 0
        curent_position = 1
        for d in self.bits_full_data:#[position : self.__full_size()]:    #
            if d == bit:
                position_size += 1
            if position_size == position:
                return curent_position
            curent_position += 1
        return -1
    
    def __get_rank(self, position=None, bit=None):
        if position==None or bit==None:
            print("Please give correct parameters")
            return -1
        rs_position = position//(BLOCKS_NUM*BITS_NUM)    #Calculate rs and rb position
        rb_position = position//BITS_NUM
        #print(rs_position,len(self.rs))

        rank = self.rs[rs_position]
        #Check if the position is at the same area, if is then ignore the rb
        if (((position % (BLOCKS_NUM*BITS_NUM)) != 0) and (((rs_position*BLOCKS_NUM) != rb_position) or (rs_position == 0)) ):
            rank += self.rb[rb_position]
        #Calculate the remaining bits
        last_position = (BITS_NUM*rb_position)
        while (last_position < position):
            value = self.bits_full_data[last_position]
            if value: 
                rank += 1
            last_position += 1
        
        if bit:             #If i look for True(1) okay return, if i look for False(0) then return the position - rank 
            return rank
        return position - rank

    def __get_leaf(self,character):        #Get the leaf where the character is 
        index = self.data.index(character)
        if self.__size() == 2:
            return self
        value = self.bits_data[index]
        if value:
            return self.childern[1].__get_leaf(character)
        return self.childern[0].__get_leaf(character)
    
    def __gen_tree(self):                       #Generate left and right child
        left = []
        right = []
        index = 0
        for data in self.bits_full_data:        #The True(1) got to the right and the False(0) go to the left
            if data:
                right.append(self.full_data[index])
            else:
                left.append(self.full_data[index])
            index += 1
        self.__add_child(Node(left, self, True))
        self.__add_child(Node(right, self, False))
    
    def __decode_data(self):                    #Decode the data
        while len(self.bits_data) != self.__size():
            if len(self.bits_data) < self.__size() /2:
                self.bits_data.append(False)
            else:
                self.bits_data.append(True)
        self.__set_bits()
    
    def __set_bits(self):                       #set the full bit
        for d in self.full_data:
            index = self.data.index(d)
            bit = self.bits_data[index]
            self.bits_full_data.append(bit)

    def __add_child(self,obj):                  #Append the child. index 0 is the left, and 1 is right
        self.childern.append(obj)
    
    def __size(self):
        return len(self.data)
    
    def __full_size(self):
        return len(self.full_data)
    
    def __get_bit(self,character=None):            #Given a character return if is True(1) or False(0)
        if character == None:
            return character
        for data in self.data:
            if character==data:
                return self.bits_data[self.data.index(data)]
        return None
        
    def __create_RRR(self):                     #Create the RRR Node that make the rank very fast
        counter = 0
        num_of_super_block = 0;
        num_of_block = 0;
        rs_counter = 0
        rb_counter = 0
        self.rb.append(rb_counter)
        for data in self.bits_full_data:        #Calculate how many True(1) have the Node, to calculate the rs and rb. rs is for the super block and rb is for the block
            if ((counter % BITS_NUM) == 0) and (counter != 0):
                self.rb.append(rb_counter)
                num_of_block += 1
                            
            if (counter % (BLOCKS_NUM * BITS_NUM) == 0):
                self.rs.append(rs_counter)
                num_of_super_block += 1
                rb_counter = 0
                
            if data:
                rs_counter += 1
                rb_counter += 1
            counter += 1
        self.rb.append(rb_counter)
        while (num_of_super_block < SUPER_BLOCK_SIZE + 1):
            self.rs.append(rs_counter)
            num_of_super_block += 1
            
    """
    Private Functions
    """                           
