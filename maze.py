from cell import *
from first_window import *
import time
import random

class Maze():

    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win=None,seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self.seed = 0
        if seed is not None:
            self.seed=random.seed(seed)
           
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
   
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                col_cells.append(cell)
            self._cells.append(col_cells)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
            
    
    def _draw_cell(self,i,j):
        # calculate x and y position of cell based on i,j and cell_size then draw the cell
        if self._win is None:
            return
        x1 = self._x1 + (j * self._cell_size_x)
        y1 = self._y1 + (i * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell = self._cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(0,0)
        self._draw_cell(self._num_cols-1,self._num_rows-1)
    
    def _break_walls_r(self,i,j):
        self._cells[i][j].visited=True

        while True:
            neighbors = []
            if i>0 and self._cells[i-1][j].visited==False:
                neighbors.append((i-1,j))
            if i<self._num_cols-1 and self._cells[i+1][j].visited==False:
                neighbors.append((i+1,j))
            if j>0 and self._cells[i][j-1].visited==False:
                neighbors.append((i,j-1))
            if j<self._num_rows-1 and self._cells[i][j+1].visited==False:
                neighbors.append((i,j+1))
            
            
            if len(neighbors)==0:
                self._draw_cell(i,j)
                return
            
            # pick random direction and knock down wall between current cell and chosen cell
            index=random.randint(0,len(neighbors)-1)
            new_i,new_j = neighbors[index]
            #break wall between i,j and new_i,new_j
            if new_i>=0 and new_i<self._num_cols and new_j>=0 and new_j<self._num_rows:
                if self._cells[new_i][new_j].visited==False:
                    if new_i==i-1:
                        self._cells[i][j].has_top_wall=False
                        self._cells[new_i][new_j].has_bottom_wall=False
                    if new_i==i+1:
                        self._cells[i][j].has_bottom_wall=False
                        self._cells[new_i][new_j].has_top_wall=False
                    if new_j==j-1:
                        self._cells[i][j].has_left_wall=False
                        self._cells[new_i][new_j].has_right_wall=False
                    if new_j==j+1:
                        self._cells[i][j].has_right_wall=False
                        self._cells[new_i][new_j].has_left_wall=False
                    self._draw_cell(i,j)
                    self._draw_cell(new_i,new_j)
                    self._break_walls_r(new_i,new_j)
            

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited=False


        
