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

def showEndInterface( screen, width, height ):
    screen.fill( configuration.BACKGROUND_COLOR )
    font = pygame.font.Font( configuration.FONTPATH, width/15 )
    title = font.render( 'Good job, you won!', True, ( 233, 150, 122 ) )
    rect = title.get_rect()
    rect.midtop = ( width/2, height/2.5 )
    screen.blit( title, rect )
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if( event.type == pygame.QUIT ) or ( event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE ):
                pygame.quit()
                sys.exit()
        pygame.display.update()

def showStartInterface( screen, width, height ):
    screen.fill( configuration.BACKGROUND_COLOR )
    t_font = pygame.font.Font( configuration.FONTPATH, width/4 ) # el puso // en vez de /
    c_font = pygame.font.Font( configuration.FONTPATH, width/20 ) #

    title = t_font.render( 'Puzzle', True, configuration.RED )
    content1 = c_font.render( 'Press H, M or L to choose your puzzle', True, configuration.BLUE )
    content2 = c_font.render( 'H-5x5, M-4x4, L-3x3', True, configuration.BLUE )
    t_rect = title.get_rect()
    t_rect.midtop = ( width/2, height/10 )
    c_rect1 = content1.get()
    c_rect1.midtop = ( width/2, height/2.2 )
    c_rect2 = content2.get()
    c_rect2.midtop = ( width/2, height/1.8 )

    screen.blit( title, t_rect )
    screen.blit( content1, c_rect1 )
    screen.blit( content2, c_rect2 )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or ( event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE ):
                pygame.quit()
                sys.exit
            elif event.type == pygame.KEYDOWN:
                if event.key == ord( 'l' ): return 3
                elif event.key == ord( 'm' ): return 4
                elif event.key == ord( 'h' ): return 5
        pygame.display.update()