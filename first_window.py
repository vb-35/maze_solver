from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self,width, height):
        self.width=width
        self.height=height
        self.__root=Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack()
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


def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__=='__main__':
    main()