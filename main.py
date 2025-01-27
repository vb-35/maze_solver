from first_window import *
from cell import *
from maze import *
import sys

def main():
    sys.setrecursionlimit(10000)
    num_rows = 10
    num_cols = 10
    margin =50
    screen_width = 800
    screen_height = 800

    cell_size_x = (screen_width - 2*margin) // num_cols
    cell_size_y = (screen_height - 2*margin) // num_rows
    win = Window(screen_width, screen_height)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    solvable=maze.solve()
    if not solvable:
        print("Maze is not solvable")
    else:
        print("Maze solved")
        
    win.wait_for_close()


if __name__=='__main__':
    main()