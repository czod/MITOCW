# 6.00 Problem Set 11
#
# graph.py
#
# A set of data structures to represent graphs
#
import copy

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
       self.src = src
       self.dest = dest
   def getSource(self):
       return self.src
   def getDestination(self):
       return self.dest
##   def __str__(self):
##       return str(self.src) + '->' + str(self.dest)
      
class WeightedEdge(Edge):
      """ The weightList is a list[] of weights associated with the edge, positive values increase the edge weight,
   negative values decrease it."""
   def __init__(self,src,dest,weightList):
      Edge.__init__(self,src,dest)
      self.weightList = weightList
      self.arc = (src,dest)

   def getWeights(self):
      return self.weightList

   def getArc(self):
      return self.arc

class Digraph(object):
   """
   A directed graph
   """
   def __init__(self):
       self.nodes = set([])
       self.edges = {}
       self.wEdges = {}
   def addNode(self, node):
      if self.hasNode(node):
         raise ValueError('Duplicate Node')
      else:
         self.nodes.add(node)
         self.edges[node] = []
      
   def addEdge(self, edge):
       src = edge.getSource()
       dest = edge.getDestination()
##       if not(src in self.nodes and dest in self.nodes):
##           raise ValueError('Node not in graph')
       for i in self.edges.iterkeys():
          if src.__eq__(i):
             for j in range(len(self.edges[i])):
                if dest.__eq__(self.edges[i][j]):
                   break
             self.edges[i].append(dest)

   def addWEdge(self,edge):
      src = edge.getSource()
      dest = edge.getDestination()
      weights = weightedEdge.getWeights()
      wArc = weightedEdge.getArc()
      for i in self.edges.iterkeys():
         if src.__eq__(i):
            for j in range(len(self.edges[i])):
               if dest.__eq__(self.edges[i][j]):
                  break
            self.edges[i].append(dest)
            self.weightedEdges[wArc] = weights

   def getWEdge(self,src,dest):
      if not self.hasNode(src):
         raise ValueError('Node not in graph')
      if not self.hasNode(dest):
         raise ValueError('Node not in graph')
      wArc = (src,dest)
      return self.weightedEdges[wArc]

   def childrenOf(self, node):
       return self.edges[node]
   def hasNode(self, node):
      for i in self.nodes:
         if i.__eq__(node):
            print i,node,True
            return True

   def __str__(self):
       res = ''
       for k in self.edges:
           for d in self.edges[k]:
               res = res + str(k) + '->' + str(d) + '\n'
       return res[:-1]

