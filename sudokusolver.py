
#validates the whole table
def validates(value,position):
    if board[position[0]].count(value) > 0:
        return False
    else:
        count = 0
        for i in range(0,9):
            if board[i][position[1]] == value:
                count += 1
        if count > 0:
            #print(count)
            return False
    #evaluates square
    if position[0] in range(0,3):
        x = [0,1,2]
    elif position[0] in range(3,6):
        x = [3,4,5] 
    else:
        x = [6,7,8]
    if position[1] in range(0,3):
        y = [0,1,2]
    elif position[1] in range(3,6):
        y = [3,4,5] 
    else:
        y = [6,7,8]
    count_2 = 0
    for i in x:
        for j in y:
            if value == board[i][j]:
                count_2 += 1
    if count_2 > 0:
        return False
    return True

def validateInitial(position):
    options = []
    for i in range(1,10):
        if validates(i,position):
            options.append(i)
    return options
        

def find_zeros():
    positions = []
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j] == 0:
                options = validateInitial((i,j))
                positions.append([(i,j),options]) 
    return positions
    

def solution(index):
    if index < len(positions_list): 
        x = positions_list[index][0][0]
        y = positions_list[index][0][1] 
        for i in positions_list[index][1]:           
            #print(str(x),str(y))                                         
            if validates(i,positions_list[index][0]):
                log.write('sol:'+str(i)+'\n')                
                board[x][y]=i
                if solution(index+1):
                    return True
            board[x][y]=0
    else:
        return True
                         
    

                 

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

print(board)

positions_list = find_zeros()
print(positions_list)
#print(len(positions_list))
solution(0)
print(board)
