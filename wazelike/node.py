class Node(object):
    """class that represent a nod which have geographic position (x,y) and delay time(red light)"""
    ID=0
    ##initializing the variables
    def __init__ (self,GeoX,GeoY,delayTime=0,name=''):
        self.id=Node.ID
        Node.ID=Node.ID+1
        self.GeoX=GeoX
        self.GeoY=GeoY
        self.delayTime=delayTime
        self.name=name
            
    ## return string of the object
    def str(self):
        st='node #{0}: {1} - ({2},{3}) with delay time of {4} min'.format(self.id,self.name,self.GeoX,self.GeoY,self.delayTime)
        return st
    
    def __eq__(self,other):
        return(self.id==other.id)