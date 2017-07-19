import tkinter as tk
from tkinter.messagebox import *
from tkinter.filedialog import *
import Eqn_solver.main as eqn


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.mainframe = tk.Frame(self.parent, height=600, width=600)
        self.mainframe.pack()
        MenuBar(self.parent)


class MenuBar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.menubar = tk.Menu(self.parent)
        self.filemenucascade()
        self.parent.config(menu=self.menubar)

    def filemenucascade(self):
        self.menubar.add_command(label="Quit!", command=self.parent.quit)


class CodeWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.text = CustomText(self)
        # self.vsb = tkinter.Scrollbar(orient="vertical", command=self.text.yview)
        # self.text.configure(yscrollcommand=self.vsb.set)
        self.text.configure()
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)

        # self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="left", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

    def _on_change(self, event):
        self.linenumbers.redraw()

    def solvecode(self, codetext, outputtext):
        inputstring = codetext.text.get("1.0", END)
        outputtext.delete(1.0, END)
        try:
            if isinstance(inputstring, str):
                resultsout = eqn.main(inputstring)
                outputtext.insert(1.0, resultsout)

        except:
            resultsout = "Error in Solving, \nwill give more information tommorow"
            outputtext.insert(1.0, resultsout)

    def printtogui(self, solveroutput, outputtext):
        outputtext.text.insert(1.0, solveroutput)

    def __quitApplication(self):
        self.parent.destroy()
        # exit()

    def __showAbout(self):
        showinfo("App", "all the bugs\nVersion 0.1")

    def __openFile(self, opentext):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self.__file == "":
            # no file to open
            self.__file = None
        else:
            # try to open the file
            # set the window title
            self.parent.title(os.path.basename(self.__file) + " - Equation Solver")
            opentext.text.delete(1.0, END)

            file = open(self.__file, "r")

            opentext.text.insert(1.0, file.read())

            file.close()

    def __newFile(self, newtext):
        self.parent.title("Untitled - Equation Solver")
        self.__file = None
        newtext.text.delete(1.0, END)

    def __saveFile(self, savedtext):
        if self.__file == None:
            # save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                # try to save the file
                file = open(self.__file, "w")
                file.write(savedtext.text.get(1.0, END))
                file.close()
                # change the window title
                self.parent.title(os.path.basename(self.__file) + " - Equation Solver")
        else:
            file = open(self.__file, "w")
            file.write(savedtext.text.get(1.0, END))
            file.close()


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
