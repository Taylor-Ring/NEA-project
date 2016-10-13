import tkinter as tk


class Application():
    def __init__(self):
        self.root = tk.Tk()
        Bquit = tk.Button(self.root, text = "quit", command = self.quitMW)
        Bcreate = tk.Button(self.root, text = "create grid")
        Brandom = tk.Button(self.root, text = "create random")
        Bhelp = tk.Button(self.root, text = "help")
        Lwelcome = tk.Label(self.root, text = """welcome to the transportation
problem solver!""")
        Lrows = tk.Label(self.root,text = "rows")
        Lcolumns = tk.Label(self.root,text = "columns")
        Erows = tk.Entry(self.root)
        Ecolumns  = tk.Entry(self.root)

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

    def quitMW(self):
        self.root.destroy()
        

app = Application()
