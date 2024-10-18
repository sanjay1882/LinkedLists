class Node:
  
   def __init__(self,data):
        self.data=data
        self.pointer=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def add(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode 
        else:
            cur=self.head
            while (cur.pointer is not None):
                cur=cur.pointer
            cur.pointer=newnode
    def print(self):
        cur=self.head
        while (cur is not None):
            print(cur.data,end="")
            cur=cur.pointer
    def remove(self,data):
        if (self.head is not None):
            if (self.head.data ==data):
                self.head=self.head.pointer
                print("removed",data)
        else:
            print("list is empty")
linkedlist=Linkedlist()
linkedlist.add(20)
linkedlist.remove(20)
linkedlist.print()
    
