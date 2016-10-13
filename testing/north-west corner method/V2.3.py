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

print(Gcells[0].info())

supplyHold = supply[Gcells[0].row - 1]
demandHold = demand[Gcells[0].column - 1]

print(supplyHold)
print(demandHold)

leftOverStock = supplyHold - demandHold
if leftOverStock < 0:
    leftOverStock = 0

leftOverDemand = demandHold - supplyHold
if leftOverDemand < 0:
    leftOverDemand = 0

if leftOverDemand == 0:
    Gcells[0].stock = demandHold
else:
    Gcells[0].stock = abs(supplyHold - demandHold)
    

supply[Gcells[0].row] = leftOverStock
demand[Gcells[0].column] = leftOverDemand

print(supply[Gcells[0].row])
print(demand[Gcells[0].column])
Gcells[0].info()







#for i in range(len(Gcells)):
#    Gcells[i].info()




