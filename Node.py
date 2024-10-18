#Creating a Node

class Node:
  
   def __init__(self,data):
        self.data=data
        self.pointer=None
        

linkedlist=Node()#Initailzation
linkedlist.data(10)

print(linkedlist.data)
