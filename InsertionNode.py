class Node:

   def __init__(self,data):
        self.data=data
        self.pointer=None
#craeing linked list        
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
linkedlist=Linkedlist()
linkedlist.add(20)
linkedlist.add(50)
linkedlist.add(230)
linkedlist.print()
