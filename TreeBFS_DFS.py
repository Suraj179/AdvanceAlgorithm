import random
import time
from collections import deque

def createArray(size:int)->list:
    array=[]
    print("Array: ",end="")
    for i in range(size):
        array.append(random.randint(0,999))
        print(f"{array[i]}, ", end="")
    print()
    return array

class Node:
    def __init__(self, data: int):
        self.data=data
        self.left=None
        self.right=None
    
    def __str__(self):
        return f"{self.data}"

class Stack:
    def __init__(self):
        self.stack=[]
    
    def isEmpty(self)->bool:
        return len(self.stack)<=0
    
    def push(self, node)->bool:
        self.stack.append(node)
        return True
    
    def pop(self)->Node:
        if self.isEmpty(): return None
        return self.stack.pop()
    
    def display(self):
        for i in self.stack:
            print(i, end=", ")
        print()
  
class Queue:
    def __init__(self):
        self.queue=deque()
    
    def isEmpty(self):
        return len(self.queue)<=0
    
    def enqueue(self, node):
        return self.queue.append(node)
    
    def dequeue(self):
        if self.isEmpty(): return False
        return self.queue.popleft()
    
    def display(self):
        for i in self.queue:
            print(i, end=", ")
        print()

    
class Tree:
    def __init__(self, list:list):
        self.list=list
        self.root=self.createTree()
        # self.root=self.createBinarySearchTree()
        # self.listSize=len(list)
    
    def createTree(self, i:int=0)->Node:
        size=len(self.list)
        if (i>=size): return None
        node=Node(self.list[i])
        node.left=self.createTree(i*2+1)
        node.right=self.createTree(i*2+2)
        return node
    
    def createBinarySearchTree(self):
        root=None
        for i in range(len(self.list)):
            # print(i, end=" ")
            root=self.insert(root, self.list[i])
        return root
    
    def insert(self, node:Node, data)->Node:
        if node is None:
            node=Node(data)
            # print("Node is None")
            return node
        else:
            if data<node.data:
                node.left=self.insert(node.left, data)
                # print("data to the left", end=" ")
            else:
                node.right=self.insert(node.right, data)
                # print("data to the right", end=" ")
        return node
    
    def traverse(self):
        def traverse(root:Node):
            if root==None: return
            else:
                traverse(root.left)
                print(root.data, end=", ")
                traverse(root.right)
                return
        traverse(self.root)
        print()

    def searchElement(self, data):
        pass

    def breadthFirstSearch(self, data):
        start=self.root
        goal=data

        frontier=Queue()
        frontier.enqueue(start)
        explored=Queue()

        while (not frontier.isEmpty()):

            # print(f"Frontier: ", end="")
            # frontier.display()
            # print(f"Explored: ", end="")
            # explored.display()

            node=frontier.dequeue()
            if(node.data==goal):
                print(f"{node.data} is found in tree")
                return
            
            explored.enqueue(node)
            if(node.left): frontier.enqueue(node.left)
            if(node.right):frontier.enqueue(node.right)
        else:
            print(f"{data} not found in tree")
            return
        
    def depthFirstSearch(self, data):
        start=self.root
        goal=data

        frontier=Stack()
        frontier.push(start)
        explored=Queue()

        while (not frontier.isEmpty()):

            # print(f"Frontier: ", end="")
            # frontier.display()
            # print(f"Explored: ", end="")
            # explored.display()

            node=frontier.pop()
            if(node.data==goal):
                print(f"{node.data} is found in tree")
                return
            
            explored.enqueue(node)
            if(node.right):frontier.push(node.right)
            if(node.left): frontier.push(node.left)
            
        else:
            print(f"{data} not found in tree")
            return


def main():
    size=int(input("Enter Size: "))
    array=createArray(size)
    t1=Tree(array)
    # t1.traverse()
    searchEle=23
    
    exeStart=time.perf_counter()
    t1.breadthFirstSearch(searchEle)
    exeEnd=time.perf_counter()
    print(f"BFS exe: {exeEnd-exeStart:.6f} seconds")

    exeStart=time.perf_counter()
    t1.depthFirstSearch(searchEle)
    exeEnd=time.perf_counter()
    print(f"DFS exe: {exeEnd-exeStart:.6f} seconds")
    
if __name__ == "__main__":
    main()
