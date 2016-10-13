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
        elif which == 2:
            tk.messagebox.showwarning("invalid values",""" the values you entered are not numbers or no value has been entered at all.please try again. if you need more help, please click the help button.""")

    def about(self): # this is basic info about what the program is.
        tk.messagebox.showinfo("about","""this is the transportation problem solver that uses the north-west corner method and finds the optimal solution using other methods as well.

by: Taylor Ring
version: 1.1 """)
        

    # this checks if the values entered by the user can be used for the solver. 
    def check(self,which):
        try:
            x = int(self.rows.get()) # if an error occurs when changing the text into intergers, then a warning will pop up saying that the values were not "numbers".
            #print(x)
            y = int(self.columns.get())
            #print(y)
            if (x >= 3 and x <= 10): # this checks if the numbers are in range, if not a error is rasied.
                if y >= 3 and y<= 10:
                    if which == 1:
                        return self.CgridWindow() # this will call the create grid function, leading the user to create the grid.
                    if which == 2:
                        return self.RgridWindow() # this will call the random grid function, leading the user to view a randomly-ish generated grid.
        
            raise ValueError(" not in boundries")# a error is manually raised if the values are not in range. without this, the try...except will classify the numbers as "fine" which are noot in this case.
        except:
            self.warnings(1)


    def CgridWindow(self):
        self.Cgrid = tk.Toplevel()
        counter = 0
        namesRow = []
        namesColumn = []
        EntryPlace = []
        EntryValues = []

        for i in range(int(self.rows.get())):
            namesRow.append("S"+str(i+1))
        namesRow.append("DEMAND")

        for i in range(int(self.columns.get())):
            namesColumn.append("D"+str(i+1))
        namesColumn.append("SUPPLY")

        
        frames = []
        for a in range(int(self.rows.get())*2 + 3):
            for b in range(int(self.columns.get())*2 + 3):
                cords = str(a+1)+","+str(b+1)
                #frames.append(cords)
                frames.append(tk.Frame(self.Cgrid))
                frames[counter].grid(row = a, column = b)
                counter += 1

        frames[0] = tk.Label(frames[0],text = "X")
        #print(namesColumn)
        nameCounter = 0
        for i in range(1,int(self.columns.get())*2 + 2,2):
            frames[i] = tk.Label(frames[i],text = "|")
            frames[i+1] = tk.Label(frames[i+1],text = namesColumn[nameCounter])
            nameCounter += 1
            #print(nameCounter)

        #for i in range(2,int(self.columns.get())*2 + 3,2):
            

        for a in range(1,int(self.rows.get())*2 + 3,2):
            for b in range(int(self.columns.get())*2 +3):
                frames[a*(int(self.columns.get())*2+3)+b] = tk.Label(frames[a*(int(self.columns.get())*2+3)+b],text = "-")###
                #frames[a*(int(self.columns.get())*2+3)+b+1] = tk.Label(frames[a*(int(self.columns.get())*2+3)+b+1],text = "+")###

        nameCounter = 0
        #print(namesRow)
        for a in range(2,int(self.rows.get())*2+3 - 1,2):
            frames[a*(int(self.columns.get())*2+3)] = tk.Label(frames[a*(int(self.columns.get())*2+3)],text = namesRow[nameCounter])###
            nameCounter += 1
            #print(nameCounter)
            for b in range(1,int(self.columns.get())*2+3 - 1,2):
                frames[a*(int(self.columns.get())*2+3)+b] = tk.Label(frames[a*(int(self.columns.get())*2+3)+b],text = "|")###
                frames[a*(int(self.columns.get())*2+3)+b+1] = tk.Entry(frames[a*(int(self.columns.get())*2+3)+b+1])###
                EntryPlace.append(a*(int(self.columns.get())*2+3)+b+1)

        print(int(self.rows.get())*2+3)
        last = (int(self.columns.get())*2+3)*((int(self.rows.get())*2+3) - 1)###
        frames[last] = tk.Label(frames[last], text = namesRow[-1])
        for b in range(1,int(self.columns.get())*2 + 1,2):
                frames[last+b] = tk.Label(frames[last+b],text = "|")
                frames[last+b+1] = tk.Entry(frames[last+b+1])
                EntryPlace.append(last+b+1)
                #carry = b
        frames[last+int(self.columns.get())*2 + 1] = tk.Label(frames[last+int(self.columns.get())*2 + 1], text = "|")

        counter = 0

        for a in range(int(self.rows.get())*2 + 3):
            for b in range(int(self.columns.get())*2 + 3):
                frames[counter].grid(row = a, column = b)
                counter += 1

        #print(EntryPlace)
        #for i in range(len(EntryPlace)):
        #    EntryValues.append(frames[EntryPlace[i]].get())
        #print(EntryValues)
        print(int(self.rows.get()))
        print(int(self.columns.get()))
        area = [int(self.rows.get()),int(self.columns.get())]
        

        Bsolve = tk.Button(self.Cgrid,text = "solve", command = lambda: self.transfer(EntryPlace,frames,area))
        Bsolve.grid(row = (int(self.rows.get())*2 + 4), column = 2)
    
        self.Cgrid.mainloop()
    
    def transfer(self,EntryPlace,frames,area):
        EntryValues = []
        deliveryCosts = []
        supply = []
        demand = []
        temp1 = []

        #print(self.columns.get())

        #print(len(self.columns.get()))
        
        for i in range(len(EntryPlace)):
            EntryValues.append(frames[EntryPlace[i]].get())
        print(EntryValues)
        #print(self.columns.get())


        checked = self.checkGValues(EntryValues)
        if checked == True:

            for i in range(len(EntryValues)):
                EntryValues[i] = int(EntryValues[i])



            #print(len(self.columns.get()))
            for a in range(area[0]):
                print("piE!")
                for b in range(area[1]):
                    temp1.append(EntryValues[a*(area[1]+1)+b])
                    #print(temp1)
                supply.append(EntryValues[a*(area[1]+1) + area[1]])
                deliveryCosts.append(temp1)
                temp1 = []

                
            print("supply")
            print(supply)
            print("deliveryCosts")
            print(deliveryCosts)


            for i in range(area[1]):
                demand.append(EntryValues[-area[1]+i])

                
            #demand.append(EntryValues[-4])
            #demand.append(EntryValues[-3])
            #demand.append(EntryValues[-2])
            #demand.append(EntryValues[-1])
            
            print("demand")
            print(demand)
            
    def checkGValues(self,EntryValues):
        values = EntryValues
        try:
            for number in values:
                int(number)
            return True
        except:
            self.warnings(2)
            return False
            

    def RgridWindow(self):
        print("YES. this is random. rows is " + self.rows.get() + " and columns are " + self.columns.get())

app = Application() # this starts the whole program
