# 6.00 Problem Set 11
#
# graph.py
#
# A set of data structures to represent graphs
#

class Node(object):
   def __init__(self, name):
      self.name = str(name)
   def getName(self):
      return self.name
   def __str__(self):
      return self.name
   def __repr__(self):
      return self.name
   def __eq__(self, other):
      return self.name == other.name
   def __ne__(self, other):
      return not self.__eq__(other)
   

class Edge(object):
   def __init__(self, src, dest):
       self.arc = (src,dest)
       self.src = src
       self.dest = dest
       assert type(self.src) == Node
       assert type(self.dest) == Node
       assert type(self.arc) == tuple

   def getSource(self):
       return self.src
   def getDestination(self):
       return self.dest
   def getArc(self):
       return self.arc
   def __str__(self):
       return str(self.src) + '->' + str(self.dest)

class WeightedEdge(Edge):
   """ The weightList is a list[] of weights associated with the edge, positive values increase the edge weight,
   negative values decrease it."""
   def __init__(self, src,dest,weightList):
      Edge.__init__(self,src,dest)
      self.weightList = weightList
      assert type(self.src) == Node
      assert type(self.dest) == Node
      assert type(self.weightList) == list

   def getWeights(self):
      return self.weightList

class Digraph(object):
   """
   A directed graph
   """
   def __init__(self):
      self.nodes = set([])
      self.edges = {}

   def addNode(self, node):
      assert type(node)== Node
      if node in self.nodes:
         raise ValueError('Duplicate node')
      else:
         self.nodes.add(node)
         self.edges[node] = []
         
   def addEdge(self, edge):
       src = edge.getSource()
       dest = edge.getDestination()
       assert type(edge) == Edge
       assert type(src) == Node
       assert type(dest) == Node
       
       if not(src in self.nodes and dest in self.nodes):
          print 'Node not in graph'
          raise ValueError('Node not in graph')
      ## The following line creates a list in the form [[src1,[dest1,dest2,...]],[src2,[dest1,dest2,...]],...]
         ##  This will be very useful for finding node children.
       self.edges[src].append(dest)
   def childrenOf(self, node):
      assert type(node) == Node
      return self.edges[node]
   def hasNode(self, node):
      assert type(node)==Node
      return node in self.nodes
   def __str__(self):
       res = ''
       for k in self.edges:
           for d in self.edges[k]:
               res = res + str(k) + '->' + str(d) + '\n'
       return res[:-1]

class WeightedDigraph(Digraph):
   """ I need to develop a representation of the edges where the src and dest of the edges are represented as
tuples.  I can use the tuples as dictionary indices against which I can index the weights.
"""
   def __init__(self):
      Digraph.__init__(self)
      self.weightedEdges = {}
      
      ##Since the following code doesn't actually add anything, I'm commenting it out and taking the inherited
      ## function from Digraph.  At least, I hope that's what will happen.
##   def addNode(self, node):
##      if self.nodes.__contains__(node):
##        raise ValueError('Duplicate node')
##      else:
##        self.nodes.add(node)
##        self.edges[node]=[]
   def addWeightedEdge(self, weightedEdge):
      assert type(weightedEdge) == WeightedEdge
      src = weightedEdge.getSource()
      dest = weightedEdge.getDestination()
      wArc = weightedEdge.getArc()
      weights = weightedEdge.getWeights()
      assert type(src)== Node
      assert type(dest) == Node
      assert type(wArc) == tuple
      assert type(weights) == list
##      print "src type is ", type(src)
##      print "dest type is ", type(dest)
##      print "wArc type is ", type(wArc)
##      print "weights type is ", type(weights)

      if not(src in self.nodes and dest in self.nodes):
        raise ValueError('Node not in graph')
##      self.edges[src].append(dest)
      self.weightedEdges[wArc] = weights
##      self.addEdge(Edge(src,dest))

   def getWeightedEdge(self,src,dest):
      assert type(src)== Node
      assert type(dest) == Node
      if not(src in self.nodes and dest in self.nodes):
         raise ValueError('Node not in graph')
      else:
         wArc = (src,dest)
         return self.weightedEdges[wArc]
   
   def __str__(self):
       res = ''
       for k in self.weightedEdges:
           for d in self.weightedEdges[k]:
               res = res + str(k) + '->' + str(d) + '\n'
       return res[:-1]
