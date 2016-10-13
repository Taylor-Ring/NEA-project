import tkinter as tk


class Application():
    def __init__(self):
        self.root = tk.Tk()
        self.rows = tk.StringVar()
        self.columns = tk.StringVar()
        Bquit = tk.Button(self.root, text = "quit", command = lambda: self.quits(1))
        Bcreate = tk.Button(self.root, text = "create grid", command = self.check)
        Brandom = tk.Button(self.root, text = "create random")
        Bhelp = tk.Button(self.root, text = "help")
        Lwelcome = tk.Label(self.root, text = """welcome to the transportation
problem solver!""")
        Lrows = tk.Label(self.root,text = "rows")
        Lcolumns = tk.Label(self.root,text = "columns")
        Erows = tk.Entry(self.root, textvariable = self.rows)
        Ecolumns  = tk.Entry(self.root, textvariable = self.columns)

        Lwelcome.pack()
        
        Lrows.pack()
        Erows.pack()
        
        Lcolumns.pack()
        Ecolumns.pack()
        Bcreate.pack(side = "right")
        Brandom.pack(side = "right")
        Bquit.pack(side = "left")
        Bhelp.pack(side = "left")

        self.root.mainloop()

    def quits(self,which):
        if which == 1:
            self.root.destroy()

    def check(self):
        try:
            x = int(self.rows.get())
            #print(x)
            y = int(self.columns.get())
            #print(y)
            if (x >= 3 and x <= 10):
                if y >= 3 and y<= 10:
                    #print("here!")
                    return self.goal()

            raise ValueError(" not in boundries")
        except:
            self.warnings(1)

    def warnings(self,which):
        if which == 1:
            tk.messagebox.showinfo("invalid values",""" you have either used non-numbers or numbers
that are out of range. please try again. if you need more help, please click the help button.""")

    def goal(self):
        print("YES. rows is " + self.rows.get() + " and columns are " + self.columns.get())

app = Application()
