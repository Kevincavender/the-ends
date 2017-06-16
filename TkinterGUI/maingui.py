import tkinter


class Program:
    def __init__(self, *args, **kwargs):
        self.root = tkinter.Tk()
        self.mainframe = tkinter.Frame(self.root, height=400, width=600)
        self.mainframe.pack()
        self.root.mainloop()

if __name__ == '__main__':
    Program()
