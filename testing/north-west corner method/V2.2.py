supply = [100,200,300]
deliveryCosts = [[40,47,80],[72,36,58],[24,61,71]]
demand = [200,200,200]

Gcells = []

class cellCreation():
    def __init__(self,row,column,deliveryCost):
        self.row = row
        self.column = column
        self.cost = deliveryCost
        self.stock = 0

    def info(self):
        print("row: "+str(self.row))
        print("column: "+ str(self.column))
        print("cost: "+str(self.cost))
        print("stock: "+str(self.stock))
        print(" ")


for a in range(len(deliveryCosts)):
    for b in range(len(deliveryCosts[a])):
        Gcells.append(cellCreation(a+1,b+1,deliveryCosts[a][b]))

for i in range(len(Gcells)):
    Gcells[i].info()




