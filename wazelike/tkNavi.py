from navigation import Navigation
from helpers import bgColor, make_Root, make_canvas, make_frame, Auto_Complete_Entry,BellmanFordAction

from math import sqrt
from tkinter import Toplevel,Listbox,Label, Button, StringVar 
from PIL import Image, ImageTk


class TkNavigation(Navigation):
    try:
        IMG_File=Image.open('.\\wazelike\\data\\map2.png')
    except:
        IMG_File=Image.open('.\\data\\map2.png')
    
    def __init__(self, nodesList,sectionsList):
        """initializing the variables"""
        Navigation.__init__(self,nodesList,sectionsList)
    
    def showAllNodes(self, canvas):
        """Draw all the nodes and sections in our navigation system to the canvas."""
        r=2
        for node in self.nodes:
            x=(node.GeoY-self.LOW_X)/(self.HIGH_X-self.LOW_X)*302
            y=(self.HIGH_Y- node.GeoX)/(self.HIGH_Y-self.LOW_Y)*816
            canvas.create_oval(x-r*1.25-0.5, y-r*1.25-0.5, x+r*1.25+0.5, y+r*1.25+0.5,width=0,fill='#555')
            canvas.create_oval(x-r, y-r, x+r, y+r,width=3,fill='black') 
            
        for section in self.sections:
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
        for node in self.nodes:
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
            x=(self.nodes[predecessor[i]].GeoY-self.LOW_X)/(self.HIGH_X-self.LOW_X)*302
            y=(self.HIGH_Y- self.nodes[predecessor[i]].GeoX)/(self.HIGH_Y-self.LOW_Y)*816 
            x1=(self.nodes[i].GeoY-self.LOW_X)/(self.HIGH_X-self.LOW_X)*302
            y1=(self.HIGH_Y- self.nodes[i].GeoX)/(self.HIGH_Y-self.LOW_Y)*816
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
        x=(self.nodes[end].GeoY-self.LOW_X)/(self.HIGH_X-self.LOW_X)*302
        y=(self.HIGH_Y- self.nodes[end].GeoX)/(self.HIGH_Y-self.LOW_Y)*816
        canvas.create_oval(x-r*1.25-0.5, y-r*1.25-0.5, x+r*1.25+0.5, y+r*1.25+0.5,width=0,fill='#555',tag='path')
        canvas.create_oval(x-r, y-r, x+r, y+r,width=r/2,fill='red',tag='path')
        
        x=(self.nodes[start].GeoY-self.LOW_X)/(self.HIGH_X-self.LOW_X)*302
        y=(self.HIGH_Y- self.nodes[start].GeoX)/(self.HIGH_Y-self.LOW_Y)*816
        canvas.create_oval(x-r*1.25-0.5, y-r*1.25-0.5, x+r*1.25+0.5, y+r*1.25+0.5,width=0,fill='#555',tag='path')
        canvas.create_oval(x-r, y-r, x+r, y+r,width=r/2,fill='green',tag='path')
           
    def BellmanFord(self, start,end,canvas):
        """Implements BellmanFord single source shortest path algorithm.
        Return the time the shortest path takes."""
        #initializing
        dist = [float("Inf")] * len(self.nodes)
        predecessor = [-1] * len(self.nodes)
        dist[start] = 0
        
        BellmanFordAction(dist,predecessor,self)
        # for _ in range(len(dist)):
        #     for a in self.sections:
        #         u=a.n1.id
        #         v=a.n2.id
        #         w=self.calcSectionTime(u,v)
        #         if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
        #             dist[v] = dist[u] + w
        #             predecessor[v]=u
        #         w=self.calcSectionTime(v,u)
        #         if dist[v] != float("Inf") and dist[v] + w < dist[u]: 
        #             dist[u] = dist[v] + w
        #             predecessor[u]=v
        
        self.simulatePath(start,end,predecessor,canvas)
        return dist[end]

    def navigate(self,start,end,canvas,root):
        """Navigate form start to end and set the time it took into a lable."""
        canvas.delete('path')
        if(start<0 or end<0 or start>len(self.nodes) or end>len(self.nodes) ):   # if the nodes are not in range
            lableString="\n\none or more of the cities\n you entered is not correct.\nyou may open the origin\n and destination list\nto see the avialable cities."
        else:
            a=self.BellmanFord(start,end,canvas)
            timeStr= '{0}H - {1}M - {2}S'.format(int(a/60),int(a)%60,int(a*60)%60)
            lableString = '    The time it takes to get    \n\n from {0}\nto {1}\n\nby {2} is:\n{3}.\n\n Have a safe trip!'.format(self.nodes[start].name,self.nodes[end].name,self.transport,timeStr)
        global timeLable
        timeLable=None
        try:
            timeLable.destroy() 
        except:
           "error" 
        timeLable = Label(root, text = lableString, bg='#555', font = ('calibre',15,'bold'),fg='white')
        timeLable.place(x=320, y=550)
    
    def drive(self):
        root=make_Root()
        bg=ImageTk.PhotoImage(self.IMG_File)
        canvas=make_canvas(root,bg)
        radioBnVar = StringVar(None, "1")
        frame=make_frame(root,radioBnVar,self)

        origin = Auto_Complete_Entry(frame,self.getNames())
        destination = Auto_Complete_Entry(frame,self.getNames())
        origin.entry.place(x=100, y=150)
        origin.entry.focus()
        destination.entry.place(x=100, y=200)

        startBtn=Button(frame,pady=10,padx=40, text="Start", bg=bgColor, fg='#ffffff',font= ('calibre',16,'bold'))
        startBtn['command']= lambda arg1=origin.entry_var, arg2=destination.entry_var, arg3=canvas, arg4=root: self.navigate(self.getNode(arg1.get()),self.getNode(arg2.get()),arg3,arg4)
        startBtn.place(x=70, y=410)
            
        root.mainloop()
