import tkinter
# import os
# from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import Eqn_solver.main as eqn


class Notepad(tkinter.Frame):
    def __init__(self, *args, **kwargs):
        # variables
        self.__root = Tk()
        self.frame = Frame(self.__root, padx=10, pady=10)
        self.frame.grid(column=0, row=0, columnspan=2, rowspan=1,
                        sticky=N + S + E + W)

        # self.content = Frame(self.frame, width=80, height=50)
        # self.content.grid(column=0, row=0, sticky=N + S + E + W)

        self.__thisTextArea = Frame(self.frame, width=80, height=50)
        self.__thisTextArea.grid(row=0, column=1, sticky=N + S + E + W, ipadx=100, ipady=100)

        self.codearea = CodeEditor(self.__thisTextArea)
        self.codearea.pack(side=LEFT, fill=BOTH, expand=True)

        self.__thisConsoleArea = Text(self.frame)
        self.__thisConsoleArea.grid(row=0, column=2, sticky=N + S + E + W, ipadx=200)

        self.__thisMenuBar = Menu(self.__root)
        self.__thisFileMenu = Menu(self.__thisMenuBar, tearoff=0)
        self.__thisEditMenu = Menu(self.__thisMenuBar, tearoff=0)
        self.__thisHelpMenu = Menu(self.__thisMenuBar, tearoff=0)
        self.__thisSolveButton = Button(self.__thisMenuBar)
        self.__thisScrollBar = Scrollbar(self.__thisConsoleArea)
        self.__file = None
        tkinter.Frame.__init__(self, *args, **kwargs)
        self.__root.title("Untitled - Equation Solver")
        # set icon
        try:
            self.__root.wm_iconbitmap("iconimage.ico")
            # GOT TO FIX THIS ERROR (ICON)
        except:
            pass




        # *********************************************************************
        # configure grid
        # *********************************************************************
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(0, weight=1)

        # to make the textarea auto resizable
        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_rowconfigure(0, weight=1)
        # add controls (widget)
        # *********************************************************************
        # Menu Configuration
        # *********************************************************************
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
        # ***********************************************************************
        # add vertical scroll bar
        # ***********************************************************************
        # self.__thisTextArea.config()

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        self.__thisScrollBar.config(command=self.__thisConsoleArea.yview)
        self.__thisConsoleArea.config(yscrollcommand=self.__thisScrollBar.set)


    def __solve(self):
        inputstring = self.codearea.text.get("1.0", END)
        self.__thisConsoleArea.delete(1.0, END)
        try:
            if isinstance(inputstring, str):
                resultsout = eqn.main(inputstring)
                self.__thisConsoleArea.insert(1.0, resultsout)

        except:
            resultsout = "Error in Solving, \nwill give more information tommorow"
            self.__thisConsoleArea.insert(1.0, resultsout)

    def printtogui(self, printables):
        self.codearea.text.insert(1.0, printables)

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
            self.codearea.text.delete(1.0, END)

            file = open(self.__file, "r")

            self.codearea.text.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Equation Solver")
        self.__file = None
        self.codearea.text.delete(1.0, END)

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
                file.write(self.codearea.text.get(1.0, END))
                file.close()
                # change the window title
                self.__root.title(os.path.basename(self.__file) + " - Equation Solver")
        else:
            file = open(self.__file, "w")
            file.write(self.codearea.text.get(1.0, END))
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


class TextLineNumbers(tkinter.Canvas):
    def __init__(self, *args, **kwargs):
        tkinter.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)


class CustomText(tkinter.Text):
    def __init__(self, *args, **kwargs):
        tkinter.Text.__init__(self, *args, **kwargs)

        self.tk.eval('''
            proc widget_proxy {widget widget_command args} {

                # call the real tk widget command with the real args
                set result [uplevel [linsert $args 0 $widget_command]]

                # generate the event for certain types of commands
                if {([lindex $args 0] in {insert replace delete}) ||
                    ([lrange $args 0 2] == {mark set insert}) ||
                    ([lrange $args 0 1] == {xview moveto}) ||
                    ([lrange $args 0 1] == {xview scroll}) ||
                    ([lrange $args 0 1] == {yview moveto}) ||
                    ([lrange $args 0 1] == {yview scroll})} {

                    event generate  $widget <<Change>> -when tail
                }

                # return the result from the real widget command
                return $result
            }
            ''')
        self.tk.eval('''
            rename {widget} _{widget}
            interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
        '''.format(widget=str(self)))


class CodeEditor(tkinter.Frame):
    def __init__(self, *args, **kwargs):
        tkinter.Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        # self.vsb = tkinter.Scrollbar(orient="vertical", command=self.text.yview)
        # self.text.configure(yscrollcommand=self.vsb.set)
        self.text.configure()
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)

        # self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="left", fill=BOTH, expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

    def _on_change(self, event):
        self.linenumbers.redraw()


if __name__ == "__main__":
    notepad = Notepad()
    notepad.run()
