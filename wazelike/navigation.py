from node import Node
from section import Section
from helpers import BellmanFordAction

from tkinter import Toplevel,Listbox,Label

class Navigation(object):
    """Class navigation which contain list of all the nodes and all the sections in our navigation system"""
    
    #constant Geo limits of israel's map
    HIGH_Y=33.330465
    LOW_Y= 29.479122
    HIGH_X=35.913016
    LOW_X= 34.218922

    nodes=[]
    sections=[]
    
    def __init__(self, nodesList,sectionsList):
        """initializing the variables"""
        for tup in nodesList:
            Navigation.nodes.append(Node(tup[0],tup[1],tup[2],tup[3])) 
        for tup in sectionsList:
            Navigation.sections.append(Section(Navigation.nodes[tup[0]],Navigation.nodes[tup[1]]))
        self.userSpeed=80
        self.transport="car"
    
    def getNode(self,name):
        """Search node by name.
        Return node or error value"""
        for node in Navigation.nodes:
            if node.name==name:
                return node.id
        return -1
     
    def getNames(self):
        names=[]
        for node in Navigation.nodes:
            names.append(node.name)
        return names
        
    def setSpeed(self,transport):
        """Set user transport
        Set userSpeed accordingly"""
        self.transport=transport
        if transport=="walk":
            self.userSpeed=5
        if transport=="bicycle":
            self.userSpeed=16
        if transport=="car":
            self.userSpeed=80
    
    def printAllNodes(self):
        """print all the node in our navigation system."""
        for n in Navigation.nodes:
            print(n.str())
            
    def searchSection(self,start,end):
        """Search section that contain the 2 nodes."""
        for a in Navigation.sections:
            if(a.n1.id==start and a.n2.id==end or a.n1.id==end and a.n2.id==start):
                return a
        
    def calcSectionTime(self,start,end):
        """Calculate the time between two nodes and return it."""
        if(start==end):
            return 0
        ## find the next section
        a=self.searchSection(start,end)
        dtime=0
        if(self.transport=='car'):
            dtime=a.n2.delayTime
        return a.calcAvgTime(self.userSpeed) + dtime
        
    def BellmanFord(self, start, end):
        """Implements BellmanFord single source shortest path algorithm.
        Return the time the shortest path takes."""
        #initializing
        dist = [float("Inf")] * len(Navigation.nodes)
        predecessor = [-1] * len(Navigation.nodes)
        dist[start] = 0
        
        BellmanFordAction(dist,predecessor,self)
       
        return dist[end]


     
