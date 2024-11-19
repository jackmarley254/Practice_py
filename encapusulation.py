# Data Encapsulation
class personalComputer:

    def __init__(self):
        self.maxComputerPrice = 20000
        
    def mySell(self):
        print("Selling Price: {}".format(self.maxComputerPrice))
        
    def setMaxComputerPrice(self, price):
        self.maxComputerPrice = price
        
pc = personalComputer()
pc.mySell()

# change the price
pc.maxComputerPrice = 30000
pc.mySell()

# using setter function
pc.setMaxComputerPrice(40000)
pc.mySell()