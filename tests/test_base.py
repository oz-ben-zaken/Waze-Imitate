import node
from section import Section
from navigation import Navigation
from math import sqrt

def test_node():
    n1= Node(0,0,1,'first')
    n2= Node(0,1,2,'second')
    n3= Node(1,0,1,'third')
    
    assert n1.str()=='node #0: first - (0,0) with delay time of 1 min'
    assert n1.str()=='node #1: second - (0,1) with delay time of 2 min'
    assert n1.str()=='node #2: third - (1,0) with delay time of 1 min'
    
    n4=n1
    assert n1==n4

def test_section():
    node1= Node(0,0,0,'first')
    node2= Node(0,1,1,'second')
    node3= Node(1,0,1,'third')
    
    s1=Section(node1,node2)
    s2=Section(node1,node3)
    s1.avgSpeed=50
    s2.avgSpeed=80
    
    assert s1.calcAvgTime(50)==121
    assert s1.calcAvgTime(80)==121
    assert s2.calcAvgTime(50)==121
    assert s2.calcAvgTime(80)==76
    
    s2.n1=node2
    
    assert int(s2.calcAvgTime(50))==170
    assert int(s2.calcAvgTime(80))==107
    
def test_navigation():
    nod=((0,0,0,'first'),(0,1,1,'second'),(1,1,0,'third'),(2,2,3,'forth'))
    sect=((0,1)(0,2),(1,3),(2,3))
    nav=Navigation(nod,sect)
    nav.setSpeed('bicycle')
    nav.BellmanFord(0,3)
    
    assert nav.BellmanFord(0,3)== 60*100*sqrt(2**2 + 2**2)/12
    