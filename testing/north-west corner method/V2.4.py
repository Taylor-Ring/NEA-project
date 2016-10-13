#3x3
#supply = [100,200,300]
#deliveryCosts = [[40,47,80],[72,36,58],[24,61,71]]
#demand = [200,200,200]

#3x4
#supply = [14,16,20]
#deliveryCosts =[[180,110,130,290],[190,250,150,280],[240,270,190,120]]
#demand = [11,15,14,10]

#4x3
#supply = [30,20,35,35]
#deliveryCosts = [[10,11,6],[4,5,9],[3,8,7],[11,10,9]]
#demand = [30,40,50]

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
    if supply[Gcells[i].row-1] == 0 or demand[Gcells[i].column-1] == 0:
        pass
    else:
        #print(Gcells[0].info())
        #place == Gcells[i].row

        supplyHold = supply[Gcells[i].row - 1]
        demandHold = demand[Gcells[i].column - 1]

        #print(supplyHold)
        #print(demandHold)

        leftOverStock = supplyHold - demandHold
        if leftOverStock < 0:
            leftOverStock = 0

        leftOverDemand = demandHold - supplyHold
        if leftOverDemand < 0:
            leftOverDemand = 0

        if leftOverDemand == 0:
            Gcells[i].stock = demandHold
        else:
            Gcells[i].stock = (demand[Gcells[i].column - 1]) - leftOverDemand#abs(supplyHold - demandHold)
            

        supply[Gcells[i].row - 1] = leftOverStock
        demand[Gcells[i].column - 1] = leftOverDemand

    #print(supply[Gcells[0].row])
    #print(demand[Gcells[0].column])
for i in range(len(Gcells)):
    Gcells[i].info()

#for i in range(len(Gcells)):
#    Gcells[i].info()




