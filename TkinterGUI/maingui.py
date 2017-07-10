import tkinter as tk
from tkinter.messagebox import *
from tkinter.filedialog import *
import Eqn_solver.main as eqn

# need to work on IO Class for the application
# need to pass line numbers
# and strings of the things

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # parent is expressed as root
        parent.title("Untitled - Equation Solver")
        # mainframe is the frame inside root where things happen
        mainframe = tk.Frame(parent)
        mainframe.pack(fill='both', expand=YES)
        solvebutton = tk.Button(mainframe, text="Solve")
        inputframe = CodeWindow(mainframe, 0)
        outputframe = CodeWindow(mainframe, 1)
        # vsb = tk.Scrollbar(outputframe.text, orient='vertical')
        solvebutton.pack(fill=X, padx=5, pady=5)
        inputframe.pack(side=LEFT, fill=Y, pady=10)
        outputframe.pack(side=LEFT, fill=Y, padx=10, pady=10)
        # vsb.pack(side=RIGHT, fill=BOTH, expand=YES)
        MenuBar(parent, inputframe.text, outputframe.text)


class MenuBar(tk.Frame):
    def __init__(self, parent, inputframe, outputframe, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.inputframe = inputframe
        self.outputframe = outputframe
        self.parent = parent
        self.__file = None
        menubar = tk.Menu(self.parent)
        filemenu=tk.Menu(menubar)
        helpmenu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Help", menu=helpmenu)
        filemenu.add_command(label="New", command=self.__newFile)
        filemenu.add_command(label="Open", command=self.__openFile)
        filemenu.add_command(label="Save", command=self.__saveFile)
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=self.parent.quit)
        helpmenu.add_command(label="About", command=self.__showabout)
        self.parent.config(menu=menubar)

    def __quitapplication(self):
        self.parent.destroy()
        # exit()

    def __showabout(self):
        showinfo("App", "all the bugs\nVersion 0.1")

    def __settings(self):
        pass

    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self.__file == "":
            # no file to open
            self.__file = None
        else:
            # try to open the file
            # set the window title
            self.parent.title(os.path.basename(self.__file) + " - Equation Solver")
            self.inputframe.delete(1.0, END)

            file = open(self.__file, "r")

            self.inputframe.insert(1.0, file.read())

            file.close()

    def __newFile(self):

        self.parent.title("Untitled - Equation Solver")
        self.__file = None
        self.inputframe.delete(1.0, END)
        self.outputframe.delete(1.0, END)

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
                file.write(self.inputframe.get(1.0, END))
                file.close()
                # change the window title
                self.parent.title(os.path.basename(self.__file) + " - Equation Solver")

        else:
            file = open(self.__file, "w")
            file.write(self.inputframe.get(1.0, END))
            file.close()


class OutputWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.text = Text(self)
        self.text.configure()
        self.text.insert(1.0, "Results")
        self.text.pack()


class CodeWindow(tk.Frame):
    def __init__(self, parent, vsbon, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.text = CustomText(self)
        if vsbon == 1: self.vsb = tk.Scrollbar(orient="vertical", command=self.text.yview)
        if vsbon == 1: self.text.configure(yscrollcommand=self.vsb.set)
        self.text.configure()
        self.linenumbers = TextLineNumbers(self, width=15)
        self.linenumbers.attach(self.text)
        if vsbon == 1: self.vsb.pack(side="right", fill=Y, in_=self)
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="left", fill="both", expand=True)
        # print(self.text)
        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

    def _on_change(self, event):
        self.linenumbers.redraw()

    def solvecode(self, codetext, outputtext):
        inputstring = codetext.get("1.0", END)
        outputtext.delete(1.0, END)
        try:
            if isinstance(inputstring, str):
                resultsout = eqn.main(inputstring)
                outputtext.insert(1.0, resultsout)

        except:
            resultsout = "Error in Solving, \nwill give more information tommorow"
            outputtext.insert(1.0, resultsout)

    def printtogui(self, solveroutput, outputtext):
        outputtext.insert(1.0, solveroutput)

    def text(self):
        return self.text


class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
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


class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
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



def runapp():
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()


if __name__ == '__main__':
    runapp()
