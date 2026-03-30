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
    def __init__(self,matrix:dict, root:str):
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
    
    def breathFirstSearch(self, goal:str)->Node:
        start:Node=self.root
        # print(type(start.data))
        queue=deque()
        queue.append(start)
        explore=deque()

        while queue:
            print(f"queue:{queue}   explore:{explore}")
            node:Node=queue.popleft()
            if node.data==goal:
                return node
            explore.append(node)

            for i in node.links:
                # print(f"i:{i} queue:{queue}   explore:{explore}")
                if i[0] not in explore and i[0] not in queue:
                    queue.append(i[0])
        else:
            return None
                    
matrix={
    's':[('a',1),('b',4)],
    'a':[('s',1),('c',2)],
    'b':[('s',4),('d',2)],
    'c':[('a',2),('e',3)],
    'd':[('a',5),('b',2),('e',1)],
    'e':[('c',3),('d',1),('g',2)],
    'g':[('d',6),('e',2)],
}

g1=Graph(matrix, 's')

if g1.breathFirstSearch('g'):
    print("Found")
else: print("Not found")





