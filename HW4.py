
#### name1:      oz ben zaken
#### id1:        204015614
####
#### name2:      Bar Kdoshim
#### id2:        207126897
####


import math
'''___________________1-A____________________'''
'''
#make point class
def make_Point_class():
    def __init__(self,x=0,y=0):
        self['set']('x',x)
        self['set']('y',y)
    #get functions
    def getX(self):
            return self['get']('x')
    
    def getY(self):
            return self['get']('y')
    #set functions
    def setX(self,value):
        self['set']('x',value)
    
    def setY(self,value):
        self ['set']('y',value)
        
    def Str(self):
        return '(%d,%d)' % (self['get']('x'), self['get']('y'))
    
    def distance(self,instance):
        return math.sqrt(((self['get']('x'))-(instance['get']('x')))**2+((self['get']('y'))-(instance['get']('y')))**2)
    
    return make_class({'__init__':__init__,'getX':getX,'getY':getY,'setX':setX,'setY':setY,'Str':Str,'distance':distance})

#make line class
def make_Line_class():
    def __init__(self,point1=0,point2=0):
        Point = make_Point_class()
        self['set']('p1',Point['new']())
        self['set']('p2',Point['new'](1,1))
    
    def getPoint(self,value):
        if(value==1):
            return self['get']('p1')
        elif(value==2):
            return self['get']('p2')
        else:
            print("error! Wrong value")
    
    def setPoint(self,value,x,y):
        
        if(value==1):
            Point['get']('setX')(self['get']('p1'),x)
            Point['get']('setY')(self['get']('p1'),y)
        elif(value==2):
            Point['get']('setX')(self['get']('p2'),x)
            Point['get']('setY')(self['get']('p2'),y)
        else:
            print("error! Wrong value")
            
    def sstr(self):
        p1=self['get']('getPoint')(1)
        p2=self['get']('getPoint')(2)
        m=(p2['get']('getY')()-p1['get']('getY')())/(p2['get']('getX')()-p1['get']('getX')())
        n=-(m*p1['get']('getX')())+p1['get']('getY')()
        return('y=',m,'x+',n)
        
    def isOnLine(self,point):
        p1=self['get']('getPoint')(1)
        p2=self['get']('getPoint')(2)
        m=(p2['get']('getY')()-p1['get']('getY')())/(p2['get']('getX')()-p1['get']('getX')())
        n=-(m*p1['get']('getX')())+p1['get']('getY')()
        if((point)['get']('getY')()==(((point)['get']('getX')()*m)+n)):
            return True
        return False
    
    return make_class({'__init__':__init__,'getPoint':getPoint,'setPoint':setPoint,'Str':sstr,'isOnLine':isOnLine})

#estimated line class
def  make_Estimated_Line_class():
    def __init__(self,distance=0):
        Line['get']('__init__')(self)
        self['set']('distance',distance)
    
    def setDistance(self,value):
        self['set']('distance',value)
        
    def getDistance(self):
        return self['get']('distance')
    
    def sstr(self):
        Line['get']('Str')(self)
        print(',%f'%self['get']('getDistance')())
        return
    
    def isOnLine(self,point):
        p2=Line['get']('getPoint')(self,2)
        p1=Line['get']('getPoint')(self,1)
        m=(p2['get']('getY')()-p1['get']('getY')())/(p2['get']('getX')()-p1['get']('getX')())
        n=-(m*p1['get']('getX')())+p1['get']('getY')()
        if(((Line['get']('isOnLine')(self,point))==True)or(math.fabs(m*point['get']('getX')()-point['get']('getY')()+n)/math.sqrt((m)**2+1))<=self['get']('getDistance')()):
            return True
        return False
    return make_class({'__init__':__init__,'setDistance':setDistance,'getDistance':getDistance,'Str':sstr,'isOnLine':isOnLine},Line)
       
def make_class(attributes,base_class=None):
    
    def get_value(att):
        if att in attributes:
            return attributes[att]
        elif base_class is not None:
            return base_class['get'](att)
        
    def set_value(att,value):
        attributes[att]=value
        
    def new(*args):
        return init_instance(cls,*args)
    cls={'get':get_value,'set':set_value,'new':new}
    return cls

def make_instance(cls):
    attributes={}
    def get_value(att):
        if att in attributes:
            return attributes[att]
        else:
            value=cls['get'](att)
        return bind_method(value, instance)
        
    def set_value(att,value):
        attributes[att]=value
    instance={'get':get_value,'set':set_value}
    return instance

def bind_method(value, instance):
        """Return a bound method if value is callable, or value otherwise."""
        if callable(value):
            def method(*args):
                return value(instance, *args)
            return method
        else:
            return value
def init_instance(cls,*args):
    instance=make_instance(cls)
    init= cls['get']('__init__')
    if init:
        init(instance,*args)
    return instance


        
Point = make_Point_class()
p1 = Point['new'](4,5)
print(p1['get']('Str')())
p1['get']('setY')(3)
print(p1['get']('Str')())
p2 = Point['new']() 
print(p2['get']('Str')()) 
print(p1['get']('distance')(p2))

Line = make_Line_class()
l1=Line['new']()
l1['get']('setPoint')(1,2,3)
l1['get']('setPoint')(2,8,6)
l1['get']('Str')()
p = l1['get']('getPoint')(1)
print(l1['get']('isOnLine')(p))


E_Line = make_Estimated_Line_class() 
el = E_Line["new"]() 
el['get']('setPoint')(1,1,6) 
el['get']("setPoint")(2,3,2) 
el['get']("setDistance")(5) 
el['get']("Str")()
p = Point["new"]() 
print(el['get']("isOnLine")(p))
el['get']("setDistance")(3) 
print(el['get']("isOnLine")(p)) '''


'''_________1-B_____________________________________________'''
empty_rlist=None
def make_class(attributes,base_class=None):
    """Return a new class, which is a dispatch dictionary."""
    def get_value(att):
        temp=attributes('getitem')(att)
        if temp!=None:
            return temp
        elif base_class is not None:
            return base_class('getitem')('get')(att)       
    def set_value(att,value):
        attributes('setitem')(attributes('getitem')(att),value)   
    def new(*args):
        return init_instance(cls,*args)
    cls = make_dict()
    cls('setitem')('get',get_value)
    cls('setitem')('set',set_value)
    cls('setitem')('new',new)
    return cls

def init_instance(cls,*args):
    instance=make_instance(cls)
    init= cls('getitem')('get')('__init__')
    if init:
        init(instance,*args)
    return instance

def make_instance(cls):
    attributes=make_dict()
    def get_value(att):
        if attributes('getitem')(att)!=None:
            return attributes('getitem')(att)
        else:
            value=cls('getitem')('get')(att)
        return bind_method(value, instance)  
    def set_value(att,value):
        attributes[att]=value
    instance = make_dict()
    instance('setitem')('get',get_value)
    instance('setitem')('set',set_value)
    return instance

def bind_method(value, instance):
        """Return a bound method if value is callable, or value otherwise."""
        if callable(value):
            def method(*args):
                return value(instance, *args)
            return method
        else:
            return value

def make_pair(x, y):
    """Return a function that behaves like a pair."""
    def setitem_pair(value):
        nonlocal y
        y=value
    def dispatch(m):   
        if m==0:
            return x
        elif m == 1:
            return y
        elif m == 2:
            return setitem_pair
    return dispatch

def getitem_pair(p, i):
    """Return the element at index i of pair p."""
    return p(i)

def make_dict():
    """Return a functional implementation of a dictionary"""
    records=make_mutable_rlist()
    def getitem (key):
        i=0
        length= records('length')()
        while(i<length):
            temp=records('get_item')(i)
            if(temp(0)==key):
                return temp(1)
            i=i+1
            return None
    def setitem (key,value):
        i=0
        length=records('length')()
        while(i<length):
            temp=records('get_item')(i)
            if(temp(0)==key):
                temp(2)(value)
                return 
            i=i+1
        records('push_first')(make_pair(key, value))   
        
    def dispatch(massage,key=None,value=None):
        if (massage=='getitem'):
            return getitem
        elif massage=='setitem':
            return setitem
        elif massage=='keys':
            return make_pair(k for k, _ in records)
        elif massage=='values':
            return make_pair(v for _, v in records)
    return dispatch

def make_rlist(first, rest):
    """Make a recursive list from its first element and the rest."""
    return make_pair(first, rest)

def first(s):
    """Return the first element of a recursive list s."""
    return s(0)
    
def rest(s):
    """Return the rest of the elements of a recursive list s."""
    return s(1)

def len_rlist(s):
    """Return the length of recursive list s."""
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length   
 
def getitem_rlist(s, i):
    """Return the element at index i of recursive list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

def make_mutable_rlist():
    """Return a functional implementation of a mutable recursive list."""
    contents = empty_rlist
    def length():
        return len_rlist(contents)
    def get_item(index):
        return getitem_rlist(contents,index)
    def push(value):
        nonlocal contents
        contents = make_rlist(value, contents)
    def pop():
        f = first(contents)
        contents = rest(contents)
        return f
    def string():
        """returns the recursive list 'contents' as a regular list"""
        def regularList(s):
            """change the recursive list 'contents' to a regular list"""
            if(s == None):
                return []
            if(type(s)!=tuple):
                return s
            a,b=s # a get the first value of the list and b the rest of the list
            return [regularList(a)] + regularList(b)
        newList=regularList(contents)
        return newList #return the regular list
    def dispatch(message):
        if message == 'length':
            return length
        elif message == 'get_item':
            return get_item
        elif message == 'push_first':
            return push
        elif message == 'pop_first':
            return pop
        elif message == 'str':
            return str
    return dispatch

def make_Point_class():
    def __init__(self,x=0,y=0):
        print("im in init in point class")
        self('setitem')('x',x)
        self('setitem')('y',y)
    
    def getX(self):
            return self('getitem')('x')
    
    def getY(self):
            return self('getitem')('y')
    
    def setX(self,value):
        self('setitem')('x',value)
    
    def setY(self,value):
        self ('setitem')('y',value)
        
    def Str(self):
        return '(%d,%d)' % (self('getitem')('x'), self('getitem')('y'))
    
    def distance(self,instance):
        return math.sqrt(((self('getitem')('x'))-(instance('getitem')('x')))**2+((self('getitem')('y'))-(instance('getitem')('y')))**2)
    
    dic=make_dict()
    dic('setitem')('__init__',__init__)
    dic('setitem')('getX',getX)
    dic('setitem')('getY',getY)
    dic('setitem')('setX',setX)
    dic('setitem')('setY',setY)
    dic('setitem')('str',Str)
    dic('setitem')('distance',distance)
    return make_class(dic)
    
print()
print("Question 1 part 2")
print("Point Class")
print()     
Point = make_Point_class()
p1= Point('getitem')('new')(4,5)
print(p1('getitem')('get')('str')()) #print (4,5)
p1('getitem')('get')("setY")(3)
print(p1('getitem')('get')("str")())  #print (4,3)
p2 = Point('getitem')('new')()
print(p2('getitem')('get')("str")()) #print (0,0)
print(p1('getitem')('get')("distance")(p2)) #print 5.0       

def make_Line_class():  
    def __init__(self,point1=0,point2=0):
        Point = make_Point_class()
        self('setitem','p1',Point['new']())
        self('setitem','p2',Point['new'](1,1))
    
    def getPoint(self,value):
        if(value==1):
            return self('getitem','p1')
        elif(value==2):
            return self('getitem','p2')
        else:
            print("error! Wrong value")

    def setPoint(self,value,x,y):
        
        if(value==1):
            Point('getitem','setX')(self)('getitem','p1',x)
            Point('getitem','setY')(self)('getitem','p1',y)
        elif(value==2):
            Point('getitem','setX')(self)('getitem','p2',x)
            Point('getitem','setY')(self)('getitem','p2',y)
        else:
            print("error! Wrong value")
            
    def sstr(self):
        p1=self['get']('getPoint')(1)
        p2=self['get']('getPoint')(2)
        m=(p2['get']('getY')()-p1['get']('getY')())/(p2['get']('getX')()-p1['get']('getX')())
        n=-(m*p1['get']('getX')())+p1['get']('getY')()
        return('y=',m,'x+',n)
        
    def isOnLine(self,point):
        p1=self['get']('getPoint')(1)
        p2=self['get']('getPoint')(2)
        m=(p2['get']('getY')()-p1['get']('getY')())/(p2['get']('getX')()-p1['get']('getX')())
        n=-(m*p1['get']('getX')())+p1['get']('getY')()
        if((point)['get']('getY')()==(((point)['get']('getX')()*m)+n)):
            return True
        return False
    
    return make_class({'__init__':__init__,'getPoint':getPoint,'setPoint':setPoint,'Str':sstr,'isOnLine':isOnLine})

def  make_Estimated_Line_class():
    def __init__(self,distance=0):
        Line('getitem','__init__')(self)
        self['set']('distance',distance)
    
    def setDistance(self,value):
        self['set']('distance',value)
        
    def getDistance(self):
        return self['get']('distance')
    
    def sstr(self):
        Line('getitem','Str')(self)
        print(',%f'%self('getitem','getDistance')())
        return
    
    def isOnLine(self,point):
        p2=Line('getitem','getPoint')(self,2)
        p1=Line('getitem','getPoint')(self,1)
        m=(p2('getitem','getY')()-p1('getitem','getY')())/(p2('getitem','getX')()-p1('getitem','getX')())
        n=-(m*p1('getitem','getX')())+p1('getitem','getY')()
        if(((Line('getitem','isOnLine')(self,point))==True)or(math.fabs(m*point('getitem','getX')()-point('getitem','getY')()+n)/math.sqrt((m)**2+1))<=self('getitem','getDistance')()):
            return True
        return False
    return make_class({'__init__':__init__,'setDistance':setDistance,'getDistance':getDistance,'Str':sstr,'isOnLine':isOnLine},Line)
       







    
    dic=make_dict()
    dic('setitem')('__init__',__init__)
    dic('setitem')('getX',getX)
    dic('setitem')('getY',getY)
    dic('setitem')('setX',setX)
    dic('setitem')('setY',setY)
    dic('setitem')('str',Str)
    dic('setitem')('distance',distance)
    return make_class(dic)



'''_______________________________________T2_________________________________________________'''
'''def make_Print_Driver_singelton_class():
    #nonlocal vars
    name=""
    printer=0
    def __init__(self, Str):
        nonlocal name
        self['set']('Job',0)
        name=Str
    def getPrinter(Str):
        nonlocal name
        #check if print exist 
        if(name == ""):
            nonlocal printer
            printer=PrinterDriver["new"](Str)
            return printer
        elif(name==Str):
            return printer
        else:
            #print error message if exist print with diffrent name
            return "Error! Wrong name!"
    def activate(self,Str):
        self['set']('Job',self['get']("Job")+1)
        print("Job # {0}: File {1} is being printed".format(self['get']("Job"),Str))   
            
    return make_class({'__init__': __init__,'getPrinter': getPrinter,'activate': activate})
           
def make_class(attributes,base_class=None):
    
    def get_value(att):
        if att in attributes:
            return attributes[att]
        elif base_class is not None:
            return base_class['get'](att)
        
    def set_value(att,value):
        attributes[att]=value
        
    def new(*args):
        return init_instance(cls,*args)
    cls={'get':get_value,'set':set_value,'new':new}
    return cls
def make_instance(cls):
    attributes={}
    def get_value(att):
        if att in attributes:
            return attributes[att]
        else:
            value=cls['get'](att)
        return bind_method(value, instance)
        
    def set_value(att,value):
        attributes[att]=value
    instance={'get':get_value,'set':set_value}
    return instance

def bind_method(value, instance):
        """Return a bound method if value is callable, or value otherwise."""
        if callable(value):
            def method(*args):
                return value(instance, *args)
            return method
        else:
            return value
def init_instance(cls,*args):
    instance=make_instance(cls)
    init= cls['get']('__init__')
    if init:
        init(instance,*args)
    return instance


PrinterDriver = make_Print_Driver_singelton_class()
printer = PrinterDriver['get']("getPrinter")("myPrint")
printer['get']("activate")("myDoc\hello.py")
PrinterDriver['get']("getPrinter")("SecondPrinter")
PrinterDriver['get']("getPrinter")("myPrint")['get']("activate")("targil.docx") '''

'''______________________________________T3_________________________________________________'''
'''import random
from math import sqrt

nodesList=((31.251764, 34.791202, 3), (31.252042, 34.786731, 2),
(31.251679, 34.793161, 1), (31.250381, 34.784395, 2),
(31.247839, 34.783515, 2), (31.246378, 34.782915, 1),
(31.245723, 34.786335, 3), (31.246487, 34.787483, 3),
(31.245117, 34.789172, 1), (31.248612, 34.789633, 2),
(31.250666, 34.790588, 1))

sectionsList=((0,1,0),(0,2,1),(1,3,0),(3,4,0),(4,5,0),(5,6,0),(7,6,1),(6,8,0),(7,9,0),(9,10,1),(10,0,0))
"""class that represent a nod which have geographic position (x,y) and delay time(red light)"""
class Node(object):
    ID=0  
    ##initializing the variables
    def __init__ (self,GeoX,GeoY,delayTime=0):
        self.id=Node.ID
        Node.ID=Node.ID+1
        self.GeoX=GeoX
        self.GeoY=GeoY
        self.delayTime=delayTime
    ## return string of the object
    def str(self):
        st='node #{0} ({1},{2})'.format(self.id,self.GeoX,self.GeoY)
        return st
    
    def __eq__(self,other):
        return(self.id==other.id)
    
"""class that represent section which contain 2 nodes, their length, and avarage speed"""
class Section(object):
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
        self.length=100*sqrt((n1.GeoX-n2.GeoX)**2 + (n1.GeoY-n2.GeoY)**2)
        self.avgSpeed=random.randint(10,80)
        
    ## print a section
    def str(self):
        print('from '+self.n1.Str()+' to '+self.n2.str())
        
    ## calculate the average time we need to pass a section
    def calcAvgTime(self, userSpeed):
        self.avgSpeed=random.randint(10,80)
        return 60*self.length/min(self.avgSpeed,userSpeed)
    
    """class that inharits from section and got 2 nodes,start and end of the section
       and contain if the section is one direction or not"""
class DirectionSection(Section):
    def __init__(self,nFrom,nTo,oneDirection):
        self.oneDirection=oneDirection
        super().__init__(nFrom,nTo)  
          
""" class navigation which contain list of all the nodes and all the sections in our navigation system"""
class Navigation(object):
    nodes=[]
    sections=[]
    ##initializing the variables
    def __init__(self,transport, nodesList,sectionsList):
        self.userspeed =0
        for tup in nodesList:
            self.nodes.append(Node(tup[0],tup[1],tup[2]))
        for tup in sectionsList:
            self.sections.append(DirectionSection(self.nodes[tup[0]],self.nodes[tup[1]],tup[2]))
        self.transport=transport
        ##for each form of transport there is an other speed
        if transport=="walk":
            self.userSpeed=10
        if transport=="car":
            self.userSpeed=random.randint(10,70)
        if transport=="bicycle":
            self.userSpeed=random.randint(8,16)
            
    """print all the node in our navigation system"""
    def printAllNodes(self):
        for n in self.nodes:
            print(n.str())
            
    ##search section that contain the 2 nodes, raise an exception if not found
    def searchSection(self,id1,id2):
        for a in self.sections:
            if(a.n1.id==id1 and a.n2.id==id2 or a.n1.id==id2 and a.n2.id==id1):
                return a
        raise
    
    ## recursive function to find how much time will the route take
    def calcRouteTime(self,start,end):  
        if(start==end):
            return 0
        ## find the next section if not found raise an exception
        a=self.searchSection(start,start+1)  
        ## route exist in the way we want
        if(a.n1==self.nodes[start] and a.n2==self.nodes[start+1]):   
            return a.calcAvgTime(self.userSpeed)+a.n2.delayTime + self.calcRouteTime(start+1,end)
        ## route exist on the other way but he is not one direction
        elif(a.n1==self.nodes[start+1] and a.n2==self.nodes[start] and a.oneDirection==False): 
            return a.calcAvgTime(self.userSpeed)+a.n1.delayTime + self.calcRouteTime(start+1,end)
        ##the route exist but he is one direction and we cant go trough him
        elif(a.n1==self.nodes[start+1] and a.n2==self.nodes[start] and a.oneDirection==True):
            raise  ##raise an exception
        
    def navigate(self,id1,id2):
        if(id1>id2):   # if the nodes are not in order
            print("please make sure you enter correct ids")
            return
        try:
            a=self.calcRouteTime(id1, id2)  # clculate the time for the route, can raise an exeption
            print('navigation time: {0} min'.format(a))
        except:
            print("No such route exists")
            
##########################################
################  driver  ################
##########################################
wise=Navigation(input('choose transportation: walk/car/bicycle: '),nodesList,sectionsList)
wise.printAllNodes()
print('navigate')
startId=int(input('from:'))
endId=int(input('to:'))
wise.navigate(startId,endId)'''