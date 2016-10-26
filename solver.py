import numpy as np
from copy import deepcopy
a = np.array([
[1,1,1],
[1,2,1],
[1,1,1]
])
b = np.array([
[2,2,3,1],
[1,2,2,2],
[1,2,1,1],
[3,1,1,1]
])
solutions = []
# print(a.shape)

# Positions counted like this
# [0,0] [1,0] [2,0]
# [0,1] [1,1] [2,1]
# [0,2] [1,2] [2,2]


def findMoves(loc, num): #location on board, number on space
    ret = []
    ret.append([loc[0],loc[1]+num])
    ret.append([loc[0],loc[1]-num])
    ret.append([loc[0]+num,loc[1]])
    ret.append([loc[0]-num,loc[1]])
    ret.append([loc[0]+num,loc[1]+num])
    ret.append([loc[0]-num,loc[1]-num])
    ret.append([loc[0]+num,loc[1]-num])
    ret.append([loc[0]-num,loc[1]+num])
    return ret

def possibleMoves(loc, num, size):
    moves = findMoves(loc, num)
    return [move for move in moves if move[0] > -1 and move[1] > -1 and move[0] < size and move[1] < size]



def moved(soln, pos):
    return pos in soln

def createPath(paths, board):
    size = board.shape[0]
    ret = []
    for path in paths:
        pos = path[-1]
        num = board[pos[0],pos[1]]
        moves = possibleMoves(pos, num, size)

        if not moves:
            # print 'No paths here'
            ret.append(path)
            continue

        for move in moves:
            if move in path:
                # print 'No backtracking'
                continue
            temp = deepcopy(path)
            temp.append(move)
            # print 'appended', temp
            ret.append(temp)

    return ret

def printPaths(paths):
    for path in paths:
        print 'Path:', path, ' Moves:', len(path)

def selectivePrint(paths, length):
    for path in paths:
        if len(path) >= length:
            print 'Path:', path, ' Moves:', len(path)

def pathComplete(path,board):
    ret = False
    pos = path[-1]
    size = board.shape[0]
    num = board[pos[0],pos[1]]
    moves = possibleMoves(pos,num,size)
    for move in moves:
        if move not in path:
            ret = True
    return not ret

def cleanup(paths,board):
    ret = []
    for path in paths:
        if pathComplete(path,board):
            solutions.append(path)
        else:
            ret.append(path)
    return ret

def solvepos(board, pos):

    paths = createPath([[pos]],board)
    paths = cleanup(paths,board)
    while paths:
        paths = createPath(paths,board)
        paths = cleanup(paths,board)

def solve(board):
    global solutions
    size = board.shape[0]
    poslist = []
    for i in range(size):
        for j in range(size):
            poslist.append([i,j])
    for pos in poslist:
        solvepos(board,pos)
    solutions = sorted(solutions, key=len)

# printPaths(createPath([[[0,0]]],b))
solvepos(a,[0,0])
selectivePrint(solutions, 0)
