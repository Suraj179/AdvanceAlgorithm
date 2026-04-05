from collections import deque
import random
import time

class Node:
    def __init__(self, data:int):
        """
        it creates Node objects
        """
        self.data=data
        self.nodeLink=[]
        self.nodeCost=[]

    def addLink(self, node, cost):
        """
        add links to the Node
        parameter:
            node is the child node
            cost is the path cost to the child node
        """
        self.nodeLink.append(node)
        self.nodeCost.append(cost)


class Graph:
    def __init__(self, NumOfNodes:int):
        """
        it creates graph object
        parameter NumOfNodes(integer)  defines the number of node in the graph
        bfsT and dfsT will be use to track execution time for BFS and DFS
        """
        self.size=NumOfNodes
        self.matrix=self.createMatrix()
        # self.displayMatrix()
        self.root=self.build_graph()
        self.bfsT=None
        self.dfsT=None

    # # it return the symmetric matrix 
    def createMatrix(self):
        """
        create the symmetric, adjacency matrix(nested list) of size associated to Graph Object
        no parameter
        return the nested list that is matrix

        to create undircted, weighted(1-9) and no self loop graph we need adgency graph in such a way that it is symmetry, and elements are not greater than 9 and all diagonal value 0
        """
        matrix=[[0 for i in range(self.size)] for i in range(self.size)]
        for row in range(len(matrix)):
            numOfLinks=random.randint(2,5)

            #this loop ensure that total number of links at each node is between 2,5
            for val in matrix[row]:
                if val!=0:
                    numOfLinks-=1
            
            #ensure it is symmetry matrix
            for link in range(numOfLinks):
                cost=random.randint(1,9) #maximum path cost will be 9
                index=random.randint(row,self.size-1)
                if index==row:
                    link-=1
                else:
                    matrix[row][index]=cost
                    matrix[index][row]=cost
        return matrix

    def displayMatrix(self):
        """
        this function will printout the matrix associated to Graph object
        no parameter
        return nothing, just print matrix
        """
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print(f"{self.matrix[i][j]}  ", end="")
            print()
    
    #index of each node is save as data inside node
    def build_graph(self)->Node:
        """
        This function creates the graph from the matrix associated with its Graph object
        no parameter
        the function will return root node
        """
        nodes=[]
        for i in range(len(self.matrix)):
            node=Node(i)
            nodes.append(node)
        
        for row in range(len(self.matrix)):
            for col in range(row+1,len(self.matrix[0])):
                if self.matrix[row][col]!=0:
                    nodes[row].addLink(nodes[col], self.matrix[row][col])
                    nodes[col].addLink(nodes[row], self.matrix[col][row])         
        return nodes[0]
    
    def breathFirstSearch(self, goal):
        """
        It preforms DFS on Graph to find goal(intger).
        parameter goal-> data to be search in graph 
        Its return None 
        Clearly prints out whether goal is found in graph or not
        It shows total cost to visited nodes
        It shows all node that were visited in search of goal
        """
        start=self.root
        queue=deque()
        costQ=deque()
        explore=deque()
        queue.append(start)
        costQ.append(0)

        cost=0
        while queue:
            node=queue.popleft()
            cost+=costQ.popleft()
            if node.data==goal:
                print(f"element found")
                break
            
            explore.append(node)

            for i in range(len(node.nodeLink)):
                if node.nodeLink[i] not in queue and node.nodeLink[i] not in explore:
                    queue.append(node.nodeLink[i])
                    costQ.append(node.nodeCost[i])
        else:
            print(f"element not found")

        print(f"total cost of visited node: {cost}")
        print("Visited Nodes: ",end="")
        for i in range(len(explore)):
            print(explore[i].data, end=", ")
        print()
        return

    #It preforms DFS on Graph to find goal(intger). its return void but clearly prints out whether goal is found in graph or not
    def depthFirstSearch(self, goal):
        """
        It preforms DFS on Graph to find goal(intger). 
        parameter goal-> data to be search in graph 
        Its return None 
        Clearly prints out whether goal is found in graph or not
        It shows total cost to visited nodes
        It shows all node that were visited in search of goal
        """
        start=self.root
        stack=deque()
        costS=deque()
        explore=deque()
        stack.append(start)
        costS.append(0)

        cost=0
        while stack:
            node=stack.pop()
            cost+=costS.pop()
            if node.data==goal:
                print(f"element found")
                break
            
            explore.append(node)

            for i in range(len(node.nodeLink)):
                if node.nodeLink[i] not in stack and node.nodeLink[i] not in explore:
                    stack.append(node.nodeLink[i])
                    costS.append(node.nodeCost[i])
        else:
            print(f"element not found")

        print(f"total cost of visited node: {cost}")
        print("Visited Nodes: ",end="")
        for i in range(len(explore)):
            print(explore[i].data, end=", ")
        print()
        return
                    
g1=Graph(10)
start=time.time()
g1.breathFirstSearch(90)
end=time.time()
g1.bfsT=round(end-start, 6)
start=time.time()
g1.depthFirstSearch(90)
end=time.time()
g1.dfsT=round(end-start, 6)


g2=Graph(1000)
start=time.time()
g2.breathFirstSearch(9000)
end=time.time()
g2.bfsT=round(end-start, 6)
start=time.time()
g2.depthFirstSearch(9000)
end=time.time()
g2.dfsT=round(end-start, 6)

g3=Graph(10000)
start=time.time()
g3.breathFirstSearch(90000)
end=time.time()
g3.bfsT=round(end-start, 6)
start=time.time()
g3.depthFirstSearch(90000)
end=time.time()
g3.dfsT=round(end-start, 6)

print(f"|   Algorithm   | BFS Exe Time (seconds)  | DFS Exe Time (seconds) |")
print(f"|   10 Nodes    |{g1.bfsT:<24} |{g1.dfsT:<24}|")
print(f"|   1000 Nodes  |{g2.bfsT:<24} |{g2.dfsT:<24}|")
print(f"|   10000 Nodes |{g3.bfsT:<24} |{g3.dfsT:<24}|")






