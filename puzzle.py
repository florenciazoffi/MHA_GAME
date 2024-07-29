import os
import sys
import configuration
import random
import pygame

def isGameOver( board, size ):
    assert isinstance( size, int ) # checking if the size of my game is the right type
    num_cells = size * size
    for i in range( num_cells - 1 ):
        if board[i] != i: return False
    return True

def moveR( board, blank_cell_idx, num_cols ):
    if blank_cell_idx % num_cols == 0: return blank_cell_idx
    board[blank_cell_idx - 1], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx - 1]
    return blank_cell_idx - 1

def moveL( board, blank_cell_idx, num_cols ):
    if ( blank_cell_idx + 1 ) % num_cols == 0: return blank_cell_idx
    board[blank_cell_idx + 1], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx + 1]
    return blank_cell_idx + 1

def moveD( board, blank_cell_idx, num_cols ):
    if blank_cell_idx < num_cols: return blank_cell_idx
    board[blank_cell_idx - num_cols], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx - num_cols]
    return blank_cell_idx - num_cols

def moveU( board, blank_cell_idx, num_cols, num_rows ):
    if blank_cell_idx >= ( ( num_rows - 1 ) * num_cols ): return blank_cell_idx
    board[blank_cell_idx + num_cols], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx + num_cols]
    return blank_cell_idx + num_cols

def createBoard( num_rows, num_cols, num_cells ):
    board = []

    for i in range( num_cells ): board.append(i)

    blank_cell_idx = num_cells - 1
    board[blank_cell_idx] = -1

    for i in range( configuration.RANDNUM ):
        direction = random.randint( 0, 4 )

        if direction == 0: blank_cell_idx = moveL( board, blank_cell_idx, num_cols )
        elif direction == 1: blank_cell_idx = moveR( board, blank_cell_idx, num_cols )
        elif direction == 2: blank_cell_idx = moveU( board, blank_cell_idx, num_cols, num_rows )
        elif direction == 3: blank_cell_idx = moveD( board, blank_cell_idx, num_cols )
    
    return board, blank_cell_idx

def getImagePaths( rootdir ):
    image_names = os.listdir( rootdir )
    assert len( image_names ) > 0
    return os.path.join( rootdir, random.choice( image_names ) )

