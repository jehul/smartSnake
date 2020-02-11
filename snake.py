BOARD_SIZE = 20
import random
import pygame
import tkinter as tk
import math
from tkinter import messagebox

'''
class Board():
    def __init__():
        self.board_size = BOARD_SIZE
        self.grid = [[0 for _ in range(board_size)] for _ in range(board_size)]
        self.snake = (random.randint(0, BOARDSIZE-1), random.randint(0, BOARDSIZE-1))
        self.length = 1
        self.food = (random.randint(0, BOARDSIZE-1), random.randint(0, BOARDSIZE-1))
        while self.food != self.snake:
            self.food = (random.randint(0, BOARDSIZE-1), random.randint(0, BOARDSIZE-1))
'''
CONST_WIDTH = 500
CONST_HEIGHT = 500
CONST_ROWS = 20
class Cube():
    x = 0
    y = 0
    

class Snake():
    pass

def drawGrid(surface):
    size_between = CONST_WIDTH // CONST_ROWS
    rgb_white = (255,255,255)
    x = 0
    y = 0
    for l in range(CONST_ROWS):
        x += size_between
        y += size_between

        pygame.draw.line(surface, rgb_white, (x,0), (x, CONST_WIDTH))
        pygame.draw.line(surface, rgb_white, (0,y), (CONST_WIDTH, y))

    
def drawWindow(surface):
    rgb_black = (0,0,0)
    surface.fill(rgb_black)
    drawGrid(surface)
    pygame.display.update()

    
def main():
    
    
    win = pygame.display.set_mode((CONST_WIDTH, CONST_HEIGHT))
    rgb_red = (255,0,0)
    start_position = (10,10)
    s = Snake(rgb_red, start_position)

    flag = True
    clock = pygame.time.clock
    
    while flag:
        pygame.time.delay(50)
        clock.tick(10)

        drawWindow(win)
