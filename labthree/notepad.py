from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, askopenfile, asksaveasfilename, asksaveasfile

omega = Tk()
omega.title("Notepad ##")
omega.geometry("600x400")

# Organize widgets in main frame
frame = Frame(omega, highlightbackground="black", highlightthickness=1, width=598, height=398, background="yellow")
frame.pack()

T = Text(frame)
T.pack()


# create methods for help sub menus
def helpme():
    T.delete(1.0, END)
    T.insert(END,
             "\n Read more about tkinter \n\n https://docs.python.org/2/library/tkinter.html\n http://www.pythonlake.com/python/tkinter")


def abouthashhash():
    T.delete(1.0, END)
    T.insert(END, "Notepad ## \n version 1.0.0\n copyright veonun@ttu.ee\n\nLicense MIT")


# Create methods for File submenus
def openfile():
    try:
        T.delete(1.0, END)
        name = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files", "*.*")), title="Choose a file.")
        omega.title(name)
        text1 = open(name).read()
        T.insert(END, text1)
        T.lift()
    except FileNotFoundError:
        messagebox.showinfo("File is not a text file")


def savefile():
    try:
        saved = asksaveasfile(mode='w', defaultextension='.txt',
                              filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
        omega.title(saved)

        if saved:
            text2 = T.get("1.0", 'end-1c')
            saved.write(text2)
            saved.close()

    except IOError:
        messagebox.showinfo("Error saving file")


def _quit():
    omega.quit()
    omega.destroy()
    exit()


# create file menu structure
menuBar = Menu(omega)
omega.config(menu=menuBar)

# create menu's for file and help for notepad ##
file = Menu(menuBar, tearoff=0)
helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File', menu=file)
menuBar.add_cascade(label='Help', menu=helpMenu)

file.add_command(label='Open', command=openfile)
file.add_command(label='Save As..', command=savefile)
file.add_separator()
file.add_command(label='Exit', command=_quit)
helpMenu.add_command(label='View Help', command=helpme)
helpMenu.add_separator()
helpMenu.add_command(label='About notepad##', command=abouthashhash)

# Starting main window omega
omega.mainloop()
