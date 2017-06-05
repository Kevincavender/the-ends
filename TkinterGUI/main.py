import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import Eqn_solver.main as Eqn

class Notepad:
    # variables
    __root = Tk()

    # default window width and height
    # __thisWidth = 300
    # __thisHeight = 300
    frame = Frame(__root, padx=10, pady=10)
    content = Frame(frame, width=100, height=50)
    __thisTextArea = Text(content)
    __thisConsoleArea = Text(content)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    __thisSolveButton = Button(__thisMenuBar)
    __thisScrollBar1 = Scrollbar(__thisTextArea)
    __thisScrollBar2 = Scrollbar(__thisConsoleArea)
    __file = None

    def __init__(self, **kwargs):
        # initialization
        # set the window text
        self.__root.title("Untitled - Equation Solver")
        # set icon
        try:
            self.__root.wm_iconbitmap("iconimage.ico")  # GOT TO FIX THIS ERROR (ICON)
        except:
            pass

        # # set window size (the default is 300x300)
        # try:
        #     self.__thisWidth = kwargs['width']
        # except KeyError:
        #     pass
        # try:
        #     self.__thisHeight = kwargs['height']
        # except KeyError:
        #     pass
        #
        # # center the window
        # screenWidth = self.__root.winfo_screenwidth()
        # screenHeight = self.__root.winfo_screenheight()
        #
        # left = (screenWidth / 2) - (self.__thisWidth / 2)
        # top = (screenHeight / 2) - (self.__thisHeight / 2)
        #
        # self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        # add text area things
        # content is also the frame
        self.frame.grid(column=0, row=0, sticky=N+S+E+W)
        self.content.grid(column=0,row=0,columnspan=2,rowspan=1,sticky=N+S+E+W)
        self.__thisTextArea.grid(row=0, column=1, sticky=N+S+E+W,ipadx = 300, ipady=300)
        self.__thisConsoleArea.grid(row=0, column=2, sticky=N+S+E+W, ipadx = 300)

        # configure grid

        self.frame.columnconfigure(0,weight=1)
        self.frame.rowconfigure(0,weight=1)
        self.content.columnconfigure(1,weight=2)
        self.content.columnconfigure(2, weight=1)
        self.content.rowconfigure(0, weight=1)

        # to make the textarea auto resizable
        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_rowconfigure(0, weight=1)
        # add controls (widget)

        self.__thisFileMenu.add_command(label="New", command=self.__newFile)
        self.__thisFileMenu.add_command(label="Open", command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit", command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)

        # self.__thisEditMenu.add_command(label="Cut", command=self.__cut)
        # self.__thisEditMenu.add_command(label="Copy", command=self.__copy)
        # self.__thisEditMenu.add_command(label="Paste", command=self.__paste)
        # self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)

        # self.__thisHelpMenu.add_command(label="About", command=self.__showAbout)
        # self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)

        self.__thisMenuBar.add_command(label="Solve", command=self.__solve)

        self.__root.config(menu=self.__thisMenuBar)
        # add vertical scroll bar
        self.__thisScrollBar1.pack(side=RIGHT, fill=Y)
        self.__thisScrollBar1.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar1.set)
        self.__thisScrollBar2.pack(side=RIGHT, fill=Y)
        self.__thisScrollBar2.config(command=self.__thisConsoleArea.yview)
        self.__thisConsoleArea.config(yscrollcommand=self.__thisScrollBar2.set)

    def __solve(self):
        inputstring = self.__thisTextArea.get("1.0", END)
        self.__thisConsoleArea.delete(1.0, END)
        if isinstance(inputstring, str):
            resultsout = Eqn.main(inputstring)
            self.__thisConsoleArea.insert(1.0, resultsout)

    def printtogui(self, printables):
        self.__thisTextArea.insert(1.0, printables)


    def __quitApplication(self):
        self.__root.destroy()
        # exit()

    def __showAbout(self):
        showinfo("App", "words go here")

    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self.__file == "":
            # no file to open
            self.__file = None
        else:
            # try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - Equation Solver")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Equation Solver")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):
        if self.__file == None:
            # save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                # try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()
                # change the window title
                self.__root.title(os.path.basename(self.__file) + " - Equation Solver")
        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):

        # run main application
        self.__root.mainloop()



# run main application
notepad = Notepad(width=800, height=600)
if __name__ == "__main__":
    notepad.run()