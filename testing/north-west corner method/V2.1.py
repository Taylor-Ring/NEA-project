supply = [100,200,300]
deliveryCosts = [[40,47,80],[72,36,58],[24,61,71]]
demand = [200,200,200]

class cell():
    def __init__(self,x,y,deliveryCost):
        self.x = x
        self.y = y
        self.cost = deliveryCost


###
first = cell(1,1,40)

print(first.x)
print(first.y)
print(first.cost)
