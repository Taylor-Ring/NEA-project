#this class will create cell objects. these will contain all of the information that
#repesent the cell. the variables and functions within the class is what is required at for this to work.
class cellCreation():
    def __init__(self,row,column,deliveryCost): # this is just implenting data from the outside into a object
        self.row = row
        self.column = column
        self.cost = deliveryCost
        self.stock = 0

    def info(self): # this is created so information can be seen. this is to make sure the program is working correctly.
        print("row: "+str(self.row))
        print("column: "+ str(self.column))
        print("cost: "+str(self.cost))
        print("stock: "+str(self.stock))
        print(" ")

# these are the selected test data being used to check the system. these all check if the program can handle different size grids and unbalanced questions
#3x3
supply = [100,200,300]
deliveryCosts = [[40,47,80],[72,36,58],[24,61,71]]
demand = [200,200,200]

#3x4
#supply = [14,16,20]
#deliveryCosts =[[180,110,130,290],[190,250,150,280],[240,270,190,120]]
#demand = [11,15,14,10]

#4x3
#supply = [30,20,35,35]
#deliveryCosts = [[10,11,6],[4,5,9],[3,8,7],[11,10,9]]
#demand = [30,40,50]

#3x3 - unbalanced
#supply = [200,200,300]
#deliveryCosts = [[40,47,80],[72,36,58],[24,61,71]]
#demand = [200,200,200]

#5x3 - unbalanced
#supply = [200, 300, 400]
#deliveryCosts = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [1, 2, 3, 4, 5]]
#demand = [100, 200, 100, 200, 100]

Gcells = [] # this will hold all of the cell objects from the grid.

rowSC = []
columnSC = []

def northWestCornerMethod(Gclls,supply,deliveryCosts,demand):

    if sum(supply) != sum(demand): # this will check if the total sum of supply is equal to the total sum of demand.
        if sum(supply) > sum(demand):
            for i in range(len(deliveryCosts)): # this just inputs the dummy column that is needed. as the deliveryCosts is organised by
                deliveryCosts[i].append(0)      # rows, this makes it easier to place cells of 0 cost
            demand.append(sum(supply)- sum(demand)) # this makes sure that the total supply equals the total demand.
        
    for a in range(len(deliveryCosts)): # this uses the data from the test data and implements it into objects, then placed in an array.
        for b in range(len(deliveryCosts[a])):
            Gcells.append(cellCreation(a+1,b+1,deliveryCosts[a][b]))

    for i in range(len(Gcells)): # this is the actual north-west corner method.
        if supply[Gcells[i].row-1] == 0 or demand[Gcells[i].column-1] == 0: # this checks weather the suppy or demand for that row/column is zero.
            pass # if it is zero, then nothing else can be done with the cells in that row/column, so they are ignored.
        else:
            #print(Gcells[0].info())
            #place == Gcells[i].row

            supplyHold = supply[Gcells[i].row - 1] # this grabs the cell's row supply
            demandHold = demand[Gcells[i].column - 1]# this grabs the cell's column demand

            #print(supplyHold)
            #print(demandHold)

            leftOverStock = supplyHold - demandHold # this calculates how much stock is left over after the transaction from the supply to demand
            if leftOverStock < 0: # if the stock left over is negative, this is just saying that the demand needs more stock but there is no more.
                leftOverStock = 0 # therefore, the left over stock is equal to zero

            leftOverDemand = demandHold - supplyHold # this is the same as the left over stock but, calculate the left over demand amount.
            if leftOverDemand < 0:
                leftOverDemand = 0 # again, if the demand amount left over is negative, this is just saying that there is more stock but the demand is full.

            if leftOverDemand == 0: # this calculates how much stock the cell actually has after the transaction.
                Gcells[i].stock = demandHold # if the left over demand is zero, then the cell is equal to the size of the demand, as it's full.
            else:
                Gcells[i].stock = (demand[Gcells[i].column - 1]) - leftOverDemand# if not, then it is the demand column take away the left over demand.
                

            supply[Gcells[i].row - 1] = leftOverStock # the left over stock and demand are then undating the supply and demand information to be carried over to the next cell
            demand[Gcells[i].column - 1] = leftOverDemand


    for i in range(len(Gcells)): # this just checks if the information is correct. this will be removed when being implemented into the final program.
        Gcells[i].info()

    return Gcells

def shadowCosts(Gcells):
    rowSC = []
    column = []
    row = 0
    columnCounter = 0
    for a in range(len(Gcells)):
        if Gcells[a].stock == 0:
            pass
        else:
            rowCounter = (Gcells[a].row) - 1
            columnCounter = (Gcells[a].column) - 1
            cost = Gcells[a].cost

            if a == 0:
                rowSC.append(0)

            if a % 2 == 0:

                columnShadowCost = cost - rowSC[rowCounter]
                columnSC.append(columnShadowCost)

            else:
            
                rowShadowCost = cost - columnSC[columnCounter]
                rowSC.append(rowShadowCost)

            print(rowSC)
            print(columnSC)
                    
            
        
    #rowSC = []
    #columnSC = []

    #rowSC.append(0)
    #cost = Gcells[0].cost
    #print(cost)

    #columnShadowCost = cost - rowSC[0]
    #columnSC.append(columnShadowCost)

    #print(rowSC)
    #print(columnSC)

    #cost = Gcells[3].cost
    #print(cost)
    #rowShadowCost = cost - columnSC[0]
    #rowSC.append(rowShadowCost) ###

    #cost = Gcells[4].cost
    #print(cost)
    #columnShadowCost = cost - rowSC[1]
    #columnSC.append(columnShadowCost)

    print(rowSC)
    print(columnSC)
    
    



### - MAIN PROGRAM - ###
Gcells = northWestCornerMethod(Gcells,supply,deliveryCosts,demand)
shadowCosts(Gcells)

