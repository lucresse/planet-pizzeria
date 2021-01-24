import numpy as np

def bug(dim,N,x,y,c):
    k = -1
    if 1< dim< 10000:
        message1 = ''
    else:
        message1 = 'wrong dimension'
        k = 0
    if 1< N< 10000:
        message2 = ''
    else:
        message2 = 'wrong pizzaria number'
        k = 0
        
    if 1<= x<= dim and 1<= y<= dim:
        message3 = ''
    else:
        message3 = 'wrong coordinate'
        k = 0
    if 1<= c<= 100:
        message4 = ''
    else:
        message4 = 'wrong capacity'
        k = 0
        
    return message1+message2+message3+message4, k

def build_block(dim, x,y,c):
    block = np.zeros((dim,dim))
    for i in range(c + 1):
        # To get vertical and horizontal
        if (x+i) < dim: # upper bound
            block[x+i][y] = 1
        if (x-i) >= 0: # lower bound
            block[x-i][y] = 1
        if (y+i) < dim:
            block[x][y+i] = 1
        if (y-i) >= 0:
            block[x][y-i] = 1

    for i in range(1,c):
        # get diagonals 
        if (x+i < dim) and (y+i < dim):
            block[x+i][y+i] = 1
        if (x-i >= 0) and (y-i >= 0): 
            block[x-i][y-i] = 1
        if (x+i < dim) and (y-i >= 0):
            block[x+i][y-i] = 1
        if (x-i >= 0) and (y+i < dim):
            block[x-i][y+i] = 1

    # flip block upside down to match indexing in question. 
    # Default indexing (0,0) on top left corner
    # Question requires indexing (0,0) at bottom left corner

    block = np.flipud(block)


    return block

def pizzerias (file_input):
    # text processing
    text = open(file_input).read().split('\n')
    line0 = text[0].split()
    
    message1 = 'The cordinates must be in between -10000 and 10000'
    message2 = 'The number of station must be in between 1 and 5000'
    # zearth coordinate
    dim = int(line0[0])
    
    N = int(line0[1])
    
    
    pizza_list = []
    
    block = np.zeros((dim,dim))

    # station coordinate's extraction
    for line in text[1:]:
        l = line.split()
        cord_i = [float(a) for a in l]
        pizza_list.append(cord_i)
    
    block = np.zeros((dim,dim))
    for elt in pizza_list:
        x,y,c = elt
        x = int(x) - 1
        y = int(y) - 1
        c = int(c)
        message, k = bug(dim, N, x+1,y+1,c)
        if k == 0:
            print(message)
            return
        block += build_block(dim,x,y,c)
    print(np.round(np.max(block),2)) 
    
pizzerias('task2_test.txt') 
