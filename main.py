from decisionTree import DecisionTree

class Main:

    def __init__(self, pathname,G):
        self.pathname = pathname
        self.G = G

    def run(self):
        dt = DecisionTree(self.pathname,self.G)
        dt.dtree()

m = Main("iris.csv",G=3)
m.run()