from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self,width, height):
        self.__root=Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()

    def wait_for_close(self):

        self.running=True
        while self.running==True:
            self.redraw()
    
    def close(self):
        self.running=False
    
    def draw_line(self,line,fill_color):
        line.draw(self.__canvas,fill_color)


class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
class Line():
    def __init__(self,pointA,pointB):
        self.pointA=pointA
        self.pointB=pointB
    
    def draw(self,canvas,fill_color):
        canvas.create_line(
    self.pointA.x, self.pointA.y, self.pointB.x, self.pointB.y, fill=fill_color, width=2)
        