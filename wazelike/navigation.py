from node import Node
from section import Section
from helpers import bgColor

from math import sqrt
from tkinter import Toplevel,Listbox,Label
from PIL import Image


class Navigation(object):
    """Class navigation which contain list of all the nodes and all the sections in our navigation system"""
    
    #constant Geo limits of israel's map
    HIGH_Y=33.330465
    LOW_Y= 29.479122
    HIGH_X=35.913016
    LOW_X= 34.218922
    IMG_File=Image.open('.\\wazelike\\data\\map2.png')
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
            
    def showAllNodes(self, canvas):
        """Draw all the nodes and sections in our navigation system to the canvas."""
        r=2
        for node in Navigation.nodes:
            x=(node.GeoY-self.LOW_X)/(self.HIGH_X-self.LOW_X)*302
            y=(self.HIGH_Y- node.GeoX)/(self.HIGH_Y-self.LOW_Y)*816
            canvas.create_oval(x-r*1.25-0.5, y-r*1.25-0.5, x+r*1.25+0.5, y+r*1.25+0.5,width=0,fill='#555')
            canvas.create_oval(x-r, y-r, x+r, y+r,width=3,fill='black') 
            
        for section in Navigation.sections:
            x0=(section.n1.GeoY-self.LOW_X)/(self.HIGH_X-self.LOW_X)*302
            y0=(self.HIGH_Y- section.n1.GeoX)/(self.HIGH_Y-self.LOW_Y)*816
            x1=(section.n2.GeoY-self.LOW_X)/(self.HIGH_X-self.LOW_X)*302
            y1=(self.HIGH_Y- section.n2.GeoX)/(self.HIGH_Y-self.LOW_Y)*816
            canvas.create_line(x0, y0, x1, y1,fill='#AAA',width=2.5)
            canvas.create_line(x0, y0, x1, y1,width=2)
     
    def showNodeList(self,root):
        """Open a window with a list of all the cities in our navigation system."""
        global listWindow
        nameList=[]
        for node in Navigation.nodes:
            nameList.append(node.name.capitalize())
        try:
            if (listWindow.state() == "normal"): listWindow.focus()
        except:
            listWindow = Toplevel()
            x=root.winfo_x()+root.winfo_width()
            y=root.winfo_y()
            listWindow.geometry('295x520+'+str(x)+'+'+str(y))
            listWindow["bg"] = bgColor
            listbox = Listbox(listWindow, height = 15, width = 18, bg = "grey", activestyle = 'dotbox', font = ("Helvetica",20),fg = "white")
            listbox.insert("end", *nameList)
            listbox.place(x=10,y=10)
         
    def simulatePath(self, start, end, predecessor, canvas):
        """Draw the path from start node to end node on the canvas.
        The path base on the the predecessor list."""
        r=3
        arroweadOffset=12
        i=end   
        while(predecessor[i]!= -1):
            arrow='last'
            x=(Navigation.nodes[predecessor[i]].GeoY-self.LOW_X)/(self.HIGH_X-self.LOW_X)*302
            y=(self.HIGH_Y- Navigation.nodes[predecessor[i]].GeoX)/(self.HIGH_Y-self.LOW_Y)*816 
            x1=(Navigation.nodes[i].GeoY-self.LOW_X)/(self.HIGH_X-self.LOW_X)*302
            y1=(self.HIGH_Y- Navigation.nodes[i].GeoX)/(self.HIGH_Y-self.LOW_Y)*816
            sectionVector=[x1-x,y1-y]
            if(sqrt(sectionVector[0]**2+sectionVector[1]**2)<=arroweadOffset*2):
                arrow='none'
            else:
                vectorSum=abs(sectionVector[0])+abs(sectionVector[1])
                xRatio=arroweadOffset*sectionVector[0]/vectorSum
                yRatio=arroweadOffset*sectionVector[1]/vectorSum
                y1=y1-yRatio
                x1=x1-xRatio
            arroweadOffset=5
            canvas.create_line(x, y, x1, y1,fill='#AAA',width=2.5,arrow= arrow,tag='path')
            canvas.create_line(x, y, x1, y1,width=2,arrow= arrow,tag='path')
            canvas.create_oval(x-r*1.25-0.5, y-r*1.25-0.5, x+r*1.25+0.5, y+r*1.25+0.5,width=0,fill='#555',tag='path')
            canvas.create_oval(x-r, y-r, x+r, y+r,width=3,fill='black',tag='path')
            i=predecessor[i]
            
        r=6
        x=(Navigation.nodes[end].GeoY-self.LOW_X)/(self.HIGH_X-self.LOW_X)*302
        y=(self.HIGH_Y- Navigation.nodes[end].GeoX)/(self.HIGH_Y-self.LOW_Y)*816
        canvas.create_oval(x-r*1.25-0.5, y-r*1.25-0.5, x+r*1.25+0.5, y+r*1.25+0.5,width=0,fill='#555',tag='path')
        canvas.create_oval(x-r, y-r, x+r, y+r,width=r/2,fill='red',tag='path')
        
        x=(Navigation.nodes[start].GeoY-self.LOW_X)/(self.HIGH_X-self.LOW_X)*302
        y=(self.HIGH_Y- Navigation.nodes[start].GeoX)/(self.HIGH_Y-self.LOW_Y)*816
        canvas.create_oval(x-r*1.25-0.5, y-r*1.25-0.5, x+r*1.25+0.5, y+r*1.25+0.5,width=0,fill='#555',tag='path')
        canvas.create_oval(x-r, y-r, x+r, y+r,width=r/2,fill='green',tag='path')
          
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
        
    def BellmanFord(self, start,end,canvas=None):
        """Implements BellmanFord single source shortest path algorithm.
        Return the time the shortest path takes."""
        #initializing
        dist = [float("Inf")] * len(Navigation.nodes)
        predecessor = [-1] * len(Navigation.nodes)
        dist[start] = 0
        
        for _ in range(len(Navigation.nodes)):
            for a in Navigation.sections:
                u=a.n1.id
                v=a.n2.id
                w=self.calcSectionTime(u,v)
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        dist[v] = dist[u] + w
                        predecessor[v]=u
                w=self.calcSectionTime(v,u)
                if dist[v] != float("Inf") and dist[v] + w < dist[u]: 
                        dist[u] = dist[v] + w
                        predecessor[u]=v
        if(canvas):
            self.simulatePath(start,end,predecessor,canvas)
        return dist[end]

    def navigate(self,start,end,canvas,root):
        """Navigate form start to end and set the time it took into a lable."""
        canvas.delete('path')
        if(start<0 or end<0 or start>Node.ID or end>Node.ID ):   # if the nodes are not in range
            lableString="\n\none or more of the cities\n you entered is not correct.\nyou may open the origin\n and destination list\nto see the avialable cities."
        else:
            a=self.BellmanFord(start,end,canvas)
            timeStr= '{0}H - {1}M - {2}S'.format(int(a/60),int(a)%60,int(a*60)%60)
            lableString = '    The time it takes to get    \n\n from {0}\nto {1}\n\nby {2} is:\n{3}.\n\n Have a safe trip!'.format(Navigation.nodes[start].name,Navigation.nodes[end].name,self.transport,timeStr)
        
        try:
            timeLable.destroy() 
        except:
           "error" 
        timeLable = Label(root, text = lableString, bg='#555', font = ('calibre',15,'bold'),fg='white')
        timeLable.place(x=320, y=550)
        
