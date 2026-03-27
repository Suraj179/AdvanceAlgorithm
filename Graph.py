from collections import deque
#for graphs with heuristic value and path cost
class Node:
    def __init__(self, data, h):
        self.data=data
        self.h=h
        self.links=[]
        self.cost=[]

    def addLink(self, node, cost):
        self.links.append(node)
        self.cost.append(cost)
    
    def __str__(self):
        return f"{self.data} "
    
    def __repr__(self):
        return f"{self.data} "

    
class Graph:
    def __init__(self):
        self.s=Node('s',7)
        self.a=Node('a',6)
        self.b=Node('b',5)
        self.c=Node('c',4)
        self.d=Node('d',3)
        self.e=Node('e',2)
        self.g=Node('g',0)

        self.s.addLink(self.a,1)
        self.s.addLink(self.b,4)
        self.a.addLink(self.s,1)
        self.a.addLink(self.c,2)
        self.a.addLink(self.d,5)
        self.b.addLink(self.s,4)
        self.b.addLink(self.d,2)
        self.c.addLink(self.a,2)
        self.c.addLink(self.e,3)
        self.d.addLink(self.a,5)
        self.d.addLink(self.b,2)
        self.d.addLink(self.e,1)
        self.d.addLink(self.g,6)
        self.e.addLink(self.c,3)
        self.e.addLink(self.d,1)
        self.e.addLink(self.g,2)
        self.g.addLink(self.d,6)
        self.g.addLink(self.e,2)

    def breathFirstSearch(self):
        start=self.s
        goal='g'

        queue=deque()
        queue.append(start)
        explored=deque()

        while queue:
            print(f"stack: {str(queue):<25}explored: {str(explored):<40}")

            node=queue.popleft()

            if node.data==goal:
                return True
            
            explored.append(node)

            for n in node.links:
                if n not in explored and n not in queue:
                    queue.append(n)
        else:
            return False
        
    def depthFirstSearch(self):
        start=self.s
        goal='g'

        stack=deque()
        stack.append(start)
        explored=deque()

        while stack:
            print(f"stack: {str(stack):<25}explored: {str(explored):<40}")

            node=stack.pop()

            if node.data==goal:
                return True
            
            explored.append(node)

            for n in node.links:
                if n not in explored and n not in stack:
                    stack.append(n)
        else:
            return False
        
    def heuristicSearch(self):
        start=self.s
        goal='g'

        explored=deque()
        priorityQ=deque()
        priorityQ.append(start)
        cost=0
        
        while priorityQ:
            # pop node with lowest heuristic value from priority queue
            node=priorityQ[0]
            # for i in priorityQ:
            #     if i.h<node.h:
            #         index=node.links.index(i)
            #         cost+=node.cost[index]
            #         node=i
            #         priorityQ.remove(i)
            
            for i in range(len(node.links)):
                if node.links[i].h<node.h:
                    cost+=node.cost[i]
                    node=node.links[i]
                    priorityQ.remove(node.links[i])
            
            if node.data==goal:
                print(f"Cost: {cost}")
                return True
            
            explored.append(node)
            print(f"stack: {str(priorityQ):<25}explored: {str(explored):<40}")
            print(node)
            for n in node.links:
                if n not in explored and n not in priorityQ:
                    priorityQ.append(n)
        else:
            return False
            
            


g1=Graph()
# if g1.breathFirstSearch():
#     print("element found")
# if g1.depthFirstSearch():
#     print("element found")
if g1.heuristicSearch():
    print("element found")
else:
    print("element Not found")


                    





