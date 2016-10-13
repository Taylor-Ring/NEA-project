import tkinter as tk

# using a class to hold the GUI for the user isbetter, as information is trnasferred easier across different windows.
#it is also a better organsier, for example the quits,helps and warnings.
class Application():
    def __init__(self):
        self.MainWindow()

    def MainWindow(self): # the windows will be in seperate functions so that they can be created again.
        # this is the widgets for the main window. where the user is putting the rows and columns.
        self.root = tk.Tk()
        self.rows = tk.StringVar()
        self.columns = tk.StringVar()
        #lambda is used so that information can be transferred while also doing the function.
        Bquit = tk.Button(self.root, text = "quit", command = lambda: self.quits(1))
        Bcreate = tk.Button(self.root, text = "create grid", command = lambda: self.check(1))
        Brandom = tk.Button(self.root, text = "create random", command = lambda: self.check(2))
        Bhelp = tk.Button(self.root, text = "help", comm = lambda: self.helps(1))
        Babout = tk.Button(self.root,text = "about", command = self.about)
        Lwelcome = tk.Label(self.root, text = """welcome to the transportation
problem solver!""")
        Lrows = tk.Label(self.root,text = "rows(suppliers)")
        Lcolumns = tk.Label(self.root,text = "columns(costomers)")
        Erows = tk.Entry(self.root, textvariable = self.rows)
        Ecolumns  = tk.Entry(self.root, textvariable = self.columns)
        #the pack placement manager has been used as the interface is not geometricly important right not.
        #this means that we can place them in order and be done.

        Lwelcome.pack()
        Lrows.pack()
        Erows.pack()
        Lcolumns.pack()
        Ecolumns.pack()
        Bcreate.pack(side = "right")
        Brandom.pack(side = "right")
        Bquit.pack(side = "left")
        Babout.pack(side = "left")
        Bhelp.pack(side = "left")

        self.root.mainloop() # this signals that there is no more widgets for the window and can finally construct the window.

    # the "quits","helps" and "warnings" functions uses a system so that different buttons can call different events from the same function.
    #this makes it more easier and quicker to place in new commands for the buttons to call. it also organise the code as well.
    def quits(self,which):# the quit function will close the window that has been called
        if which == 1:
            self.root.destroy()

    def helps(self,which): # this offers users on how to use the solver in multiple windows.
        if which == 1:
            tk.messagebox.showinfo("help","""the numbers put here will indicate the size of the problem in grid form.
for example if there are 4 suppliers and 3 costumers, then row is 4 and column is 3.
this will create a grid that will allow you to enter the individual delivery costs.
the values have to be integers and be between 3 to 10.""")

    def warnings(self,which):# this tells the user that something is wrong with values that the user placed/
        if which == 1:
            tk.messagebox.showwarning("invalid values",""" you have either used non-numbers or numbers that are out of range.
please try again. if you need more help, please click the help button.""")

    def about(self): # this is basic info about what the program is.
        tk.messagebox.showinfo("about","""this is the transportation problem solver that uses the north-west corner method and finds the optimal solution using other methods as well.

by: Taylor Ring
version: 1.1 """)
        

    # this checks if the values entered by the user can be used for the solver. 
    def check(self,which):
        return self.CgridWindow()
        #try:
        #    x = int(self.rows.get()) # if an error occurs when changing the text into intergers, then a warning will pop up saying that the values were not "numbers".
        #    #print(x)
        #    y = int(self.columns.get())
        #    #print(y)
        #    if (x >= 3 and x <= 10): # this checks if the numbers are in range, if not a error is rasied.
        #        if y >= 3 and y<= 10:
        #            if which == 1:
        #                return self.CgridWindow() # this will call the create grid function, leading the user to create the grid.
        #            if which == 2:
        #                return self.RgridWindow() # this will call the random grid function, leading the user to view a randomly-ish generated grid.
        #
        #    raise ValueError(" not in boundries")# a error is manually raised if the values are not in range. without this, the try...except will classify the numbers as "fine" which are noot in this case.
        #except:
        #    self.warnings(1)


    def CgridWindow(self):
        self.Cgrid = tk.Toplevel()
        counter = 0
        frames = []
        for a in range(int(self.rows.get())*2 + 3):
            for b in range(int(self.columns.get())*2 + 3):
                cords = str(a+1)+","+str(b+1)
                #frames.append(cords)
                frames.append(tk.Label(self.Cgrid,text = str(a+1) +","+ str(b+1)))
                frames[counter].grid(row = a, column = b)
                counter += 1

        #for i in range(1,len(frames),2):
            

        
                
        #for a in range(int(self.rows.get())*2 + 3):
        #    for b in range(int(self.columns.get())*2 +3):
        #        
        #        frames[counter].grid(row = a, column = b)
        #        counter = counter + 1
        #        #print(str(a+1)+","+str(b+1))
        self.Cgrid.mainloop()
        
    def RgridWindow(self):
        print("YES. this is random. rows is " + self.rows.get() + " and columns are " + self.columns.get())

app = Application() # this starts the whole program
