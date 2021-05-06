import random
from math import sqrt

class Section(object):
    """class that represent section which contain 2 nodes, their length, and average speed"""
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
        self.length=100*sqrt((n1.GeoX-n2.GeoX)**2 + (n1.GeoY-n2.GeoY)**2)
        self.avgSpeed=random.randint(50,80)
        
    ## print a section
    def str(self):
        print('from '+self.n1.name+' to '+self.n2.name)
        
    ## calculate the average time we need to pass a section
    def calcAvgTime(self, userSpeed):
        return 60*self.length/min(self.avgSpeed,userSpeed)