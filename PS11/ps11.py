#!/usr/bin/env /usr/bin/python -v
# 6.00 Problem Set 11
#
# ps11.py
#
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
import os
import sys
import datetime
if os.name == 'posix':
        print "smells like unix, use cwd for path"
        sys.path.append(".")
else:
        print "smells like...well, its Windows, EWW!!!"
        sys.path.append("D:\Google Drive\Education\MITOCW\PS11")

sys.setrecursionlimit(20000)
from graph import *
mapName = "mit_map.txt"
numCalls = 0
#
# Problem 2: Building up the Campus Map
#
# Write a couple of sentences describing how you will model the
# problem as a graph)
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    #TODO
    print "Loading map from file..."
    dG = Digraph()
    with open("mit_map.txt") as f:
            for line in f:
                    src,dest,dist,od=line.split()
                    src_node = Node(src)
                    dest_node = Node(dest)
                    if not dG.hasNode(src_node):dG.addNode(src_node)
                    if not dG.hasNode(dest_node):dG.addNode(dest_node)
                    weights = [dist,od]
                    edge = Edge(src_node,dest_node)
                    wEdge = WeightedEdge(src_node,dest_node,weights)
                    try:
                            dG.addEdge(edge)
                    except ValueError:
                            print "ValueError"
                    try:
                            dG.addWEdge(wEdge)
                    except ValueError:
                            print "ValueError"
    return dG
        


#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and the constraints
#


def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors,\
                     visited=[],dist=0,outDoors=0,totalDist=0,\
                     totalOutDoors=0,deBug=0):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDisOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    if deBug==3:ptDebug("The paramaters passed to the function are ",[digraph, start, end, maxTotalDist, maxDistOutdoors,visited,dist,outDoors,totalDist,totalOutDoors])
    #TODO
    # Parameter parsing and conversion
    snode = Node(start)
    enode = Node(end)

    if deBug>=2:ptDebug("Start and end nodes are ",[snode,enode])
    
    #  Parameter validation
    if not (digraph.hasNode(snode) and digraph.hasNode(enode)):
        raise ValueError('Start or end not in graph.')
    #  Begin recursion
    path = [snode]
    if snode.__eq__(enode):
        # Run done, lights out.
        # There are two ways to arrive here:
        #  1.  Both start and end nodes are the same on the first function call.
        #  2.  The function has recursed itself down to the desired end node.
        if deBug==3:ptDebug("Start and end nodes are equal ",[snode,enode])
        return path
    shortest = None
    for node in digraph.childrenOf(snode):
        if deBug>=2:ptDebug("Iterating through the children of snode ",[snode,node])
##        for j in visited:
##            if node.__eq__(node):
##                print "node has already been visited, breaking loop"
##                continue
        if not(str(node) in visited):  #cycle evasion, this will probably have to
                                # be for looped due to issues with comparison functions
                                # in the node class def.
            visited = visited + [str(node)] #presumably, creates a new list via the
                                        # the sum of the old list and the new node.
            if deBug>=2:ptDebug("Visited + node ",[visited,str(node)])
            edgeWeights = digraph.getEdgeWeight(snode,node)
            dist = dist + int(edgeWeights[0])
            outDoors = outDoors + int(edgeWeights[1])
            if deBug>=2:ptDebug("Start and end nodes are ",[snode,enode])
            newPath = bruteForceSearch(digraph,node,end,maxTotalDist,maxDistOutdoors,\
                                       visited,dist,outDoors,totalDist,totalOutDoors) #recursion initiated
            totalDist = totalDist + dist
            totalOutDoors = totalOutDoors + outDoors
            if deBug>=2:ptDebug("Total weights ",["totalDist:",totalDist,"totalOutDoors:",totalOutDoors])
            if newPath == None or totalDist > maxTotalDist or totalOutDoors > maxDistOutdoors:
                #You can only get here if during one of the recursions, no
                #path to the end node was found.  Move on to the next child.
                #If this branch is a dead end we also need to zero out the path weights associated with it.
                totalDist = totalDist - dist
                totalOutDoors = totalOutDoors - outDoors
                dist = 0
                outDoors = 0
                if deBug>=2:ptDebug("Dead end resets ",["newPath:",newPath,"totalDist:",totalDist,"totalOutDoors:",totalOutDoors])
                continue
            if (shortest == None or len(newPath) < len(shortest)):
                shortest = newPath
                if deBug>=2:ptDebug("found a new shortest path ",["newPath:",shortest])
                
    if shortest != None:
        path = path + shortest
        #if deBug>=1:ptDebug("final path ",["path:",path])
    else:
        # we end up here on the last recursion when the last node is not the
        # targetted end node.
        path = None
    return path
    

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
##def directedDFS(digraph, start, end, visited = [], memo = {}):
def directedDFS(digraph,start,end,maxTotalDist,maxDistOutdoors,visited = [],\
                memo = {},dist=0,outDoors=0,totalDist=0,totalOutDoors=0,deBug=0):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDisOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    snode = Node(start)
    enode = Node(end)
    if not (digraph.hasNode(snode) and digraph.hasNode(enode)):
        raise ValueError('Start or end not in graph.')
    path = [snode]
    if snode.__eq__(enode):
        return path
    shortest = None
    for node in digraph.childrenOf(snode):
        if (str(node) not in visited):
            visited = visited + [str(node)]
            edgeWeights = digraph.getEdgeWeight(snode,node)
            dist = dist + int(edgeWeights[0])
            outDoors = outDoors + int(edgeWeights[1])
            #print visited
            try:
                newPath = memo[node, enode]
                #memo is a dictionary containing keys in the form of
                #tuples of Nodes.  Each time a better path is found it is
                #assigned to the tuple-key until the shortest path between
                #the two nodes is identified.
                #I'm having two issues with this in the current implementation:
                #  1.  This try: block should be invoked at least once during
                #  the initial pass of this function but it isn't.
                #  2.  How do I manage weights with this...wait, I think I've
                #  figured it out.
                
            except:
                
                newPath = directedDFS(digraph,node,enode,maxTotalDist,maxDistOutdoors,
                                         visited, memo,dist,outDoors,totalDist,totalOutDoors,deBug)
                
            totalDist = totalDist + dist
            totalOutDoors = totalOutDoors + outDoors
                        
            if (newPath == None or totalDist > maxTotalDist or totalOutDoors > maxDistOutdoors):
                totalDist = totalDist - dist
                totalOutDoors = totalOutDoors - outDoors
                dist = 0
                outDoors = 0
                continue
            if (shortest == None or len(newPath) < len(shortest)):
                #print 'shortest',shortest
                #print 'newPath',newPath
                shortest = newPath
                memo[node, enode] = newPath
                #print 'memo',memo
                
    if shortest != None:
        path = path + shortest
    else:
        path = None
    return path


# Uncomment below when ready to test
if __name__ == '__main__':
    # Test cases
    digraph = load_map("mit_map.txt")

    LARGE_DIST = 1000000

    # Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    brutePath1 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
    dfsPath1 = directedDFS(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
    print "DFS: ", dfsPath1

    # Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expectedPath2 = ['32', '36', '26', '16', '56']
    brutePath2 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, 0)
    dfsPath2 = directedDFS(digraph, '32', '56', LARGE_DIST, 0)
    print "Expected: ", expectedPath2
    print "Brute-force: ", brutePath2
    print "DFS: ", dfsPath2

    # Test case 3
    print "---------------"
    print "Test case 3:"
    print "Find the shortest-path from Building 2 to 9"
    expectedPath3 = ['2', '3', '7', '9']
    brutePath3 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
    dfsPath3 = directedDFS(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath3
    print "Brute-force: ", brutePath3
    print "DFS: ", dfsPath3

    # Test case 4
    print "---------------"
    print "Test case 4:"
    print "Find the shortest-path from Building 2 to 9 without going outdoors"
    expectedPath4 = ['2', '4', '10', '13', '9']
    brutePath4 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, 0)
    dfsPath4 = directedDFS(digraph, '2', '9', LARGE_DIST, 0)
    print "Expected: ", expectedPath4
    print "Brute-force: ", brutePath4
    print "DFS: ", dfsPath4

    # Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expectedPath5 = ['1', '4', '12', '32']
    brutePath5 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
    dfsPath5 = directedDFS(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath5
    print "Brute-force: ", brutePath5
    print "DFS: ", dfsPath5

    # Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, 0)
    dfsPath6 = directedDFS(digraph, '1', '32', LARGE_DIST, 0)
    print "Expected: ", expectedPath6
    print "Brute-force: ", brutePath6
    print "DFS: ", dfsPath6

    # Test case 7
    print "---------------"
    print "Test case 7:"
    print "Find the shortest-path from Building 8 to 50 without going outdoors"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(digraph, '8', '50', LARGE_DIST, 0)
    except ValueError:
        bruteRaisedErr = 'Yes'
    
    try:
        directedDFS(digraph, '8', '50', LARGE_DIST, 0)
    except ValueError:
        dfsRaisedErr = 'Yes'
    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr

    # Test case 8
    print "---------------"
    print "Test case 8:"
    print "Find the shortest-path from Building 10 to 32 without walking"
    print "more than 100 meters in total"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(digraph, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bruteRaisedErr = 'Yes'
    
    try:
        directedDFS(digraph, '10', '32', 100, LARGE_DIST)
    except ValueError:
        dfsRaisedErr = 'Yes'
    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr


## My tests:

                
##weg=load_map(mapName)
##weg.getEdgeWeight(Node(32),Node(36))
##
###print_attributes(weg)
###print_attributes(weg.nodes)
#digraph = load_map(mapName)
##nodelist = [32, 36, 76, 57, 68, 56, 66, 18, 16, 24, 13, 26, 34, 12, 8, 4, 39, 6, 37, 31, 2, 14, 50, 10, 3, 1, 5, 7, 9, 38, 35, 33, 46, 48, 54, 62, 64]
##for i in nodelist:
##    tpath = bruteForceSearch(digraph,str(i),'36',100,100)
##    print tpath
#bpath = bruteForceSearch(digraph,'66','12',100,100)
#dpath = directedDFS(digraph,'66','12',100,100)

