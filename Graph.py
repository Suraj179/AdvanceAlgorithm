from __future__ import annotations
from collections import deque

class Node:
    def __init__(self, data: str, heuristic:int=0):
        self.data=data
        self.h=heuristic
        self.links:deque[tuple[Node, int]]=deque()
    
    def addLink(self, node:Node, cost:int):
        self.links.append((node, cost))
    
    def __str__(self):
        return f"{self.data} "
    
    def __repr__(self):
        return f"{self.data} "

class Graph:
    def __init__(self,matrix:dict, root:str, heuristicVal:list=[]):
        if len(heuristicVal)==len(matrix):
            self.root=self.createHeuristicGraph(matrix, root, heuristicVal)
        else:
            self.root=self.createGraph(matrix, root)
            
    def createGraph(self, matrix:dict, root:str,)->Node:
        for key in matrix:
            node=Node(key)
            matrix[key].append(node)
        # all the nodes has been created in above for loop
        # now create the links between the nodes
        for key in matrix:
            for i in range(len(matrix[key])-1):
                st=matrix[key][i][0]
                linkNode=matrix[st][-1]
                cost=matrix[key][i][1]
                matrix[key][-1].addLink(linkNode,cost)
        # print(matrix)
        # if matrix['e'][-1] in matrix['c'][-1].links
        return matrix[root][-1]
    
    def createHeuristicGraph(self, matrix:dict, root:str, heuristicVal:list)->Node:
        h=0
        for key in matrix:
            node=Node(key)
            node.h=heuristicVal[h]
            matrix[key].append(node)
            h+=1

        # all the nodes with heuristic value has been created in above for loop
        # now create the links between the nodes
        for key in matrix:
            for i in range(len(matrix[key])-1):
                st=matrix[key][i][0]
                linkNode=matrix[st][-1]
                cost=matrix[key][i][1]
                matrix[key][-1].addLink(linkNode,cost)
        # print(matrix)
        return matrix[root][-1]
    
    def breathFirstSearch(self, goal:str)->Node:
        start:Node=self.root
        # print(type(start.data))
        queue=deque()
        costQ=deque()
        queue.append(start)
        costQ.append(0)

        explore=deque()
        cost=0
        while queue:
            print(f"queue:{queue}   explore:{explore}")
            node:Node=queue.popleft()
            cost+=costQ.popleft()
            if node.data==goal:
                print(f"cost:{cost}")
                return node
            explore.append(node)

            for i in node.links:
                if i[0] not in explore and i[0] not in queue:
                    queue.append(i[0])
                    costQ.append(i[1])
        
        else:
            return None
        
    def depthFirstSearch(self, goal:str)->Node:
        start:Node=self.root
        stack=deque()
        costQ=deque()
        stack.append(start)
        costQ.append(0)

        explore=deque()
        cost=0
        while stack:
            print(f"stack:{stack}   explore:{explore}")
            node:Node=stack.pop()
            cost+=costQ.pop()
            if node.data==goal:
                print(f"cost:{cost}")
                return node
            explore.append(node)

            for i in node.links:
                if i[0] not in explore and i[0] not in stack:
                    stack.append(i[0])
                    costQ.append(i[1])
        else:
            return None
        
    def heuristicSearch(self, goal:str)->Node:
        start=self.root
        pQ=[]
        costQ=[]
        #node and cost value are kept corresponding at pQ and costQ
        #higher pirority goes to node with smaller h
        #higher pirority h nodes are places at the end of pQ
        #from the list, pop() is more eficient that pop(0) so higher pirority are kept in the last
        explore=deque()

        def pEnque(node:Node, cost:int):
            if len(pQ)==0:
                pQ.append(node)
                costQ.append(cost)
                return
            for i in range(len(pQ)):
                if node.h<pQ[i].h:continue
                else:
                    pQ.insert(i,node)
                    costQ.insert(i,cost)
                    break
            else:
                #not inserted 
                pQ.append(node)
                costQ.append(cost)
            return

        pEnque(start,0)
        cost=0
        while pQ:
            print(f"PirorityQueue:{pQ}   explore:{explore}")
            node:Node=pQ.pop()
            cost+=costQ.pop()
            
            if node.data==goal:
                print(f"cost:{cost}")
                return node
            explore.append(node)
            for i in node.links:
                if i[0] not in explore and i[0] not in pQ:
                    pEnque(i[0], i[1])
        else:
            return None
        

matrix={
    's':[('a',1),('b',4)],
    'a':[('s',1),('c',2),('d',5)],
    'b':[('s',4),('d',2)],
    'c':[('a',2),('e',3)],
    'd':[('a',5),('b',2),('e',1),('g',6)],
    'e':[('c',3),('d',1),('g',2)],
    'g':[('d',6),('e',2)],
}
heuristicVal=[7,6,5,4,3,2,0]
g1=Graph(matrix, 's', heuristicVal)

if g1.breathFirstSearch('g'):
    print("Found")
else: print("Not found")
if g1.depthFirstSearch('g'):
    print("Found")
else: print("Not found")
if g1.heuristicSearch('g'):
    print("Found")
else: print("Not found")

