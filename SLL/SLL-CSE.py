class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
        self.temp=None 
    def creation(self):
        num=int(input("Enter the no of nodes:"))
        for i in range(num):
            data=int(input("enter the data for nodes:"))
            newnode=Node(data)
            if self.head is None:
                self.head=newnode
                self.temp=newnode
            else: 
                self.temp.next=newnode
                self.temp=newnode
    def display(self):
        self.temp=self.head
        while self.temp is not None:
            print(self.temp.data,end="->")
            self.temp=self.temp.next
            print("None")
    def insertAtBeg(self):
        data=int(input("enter the data"))
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def insertAtEnd(self):
        data=int(input("enter the data"))
        newnode=Node(data)
        self.temp=self.head
        while self.temp.next is not None:
            self.temp=self.temp.next
        self.temp.next=newnode
    def insertAtmid(self):
        data=int(input("enter the data"));
        newnode=Node(data)
        self.temp=self.head
        pos=int(input("enter the pos"))
        for i in range(pos-1):
            prev=self.temp
            self.temp=self.temp.next
        newnode.next=self.temp
        prev.next=newnode
    def deletionAtBeg(self):
        temp=self.head
        self.head=temp.next
        self.temp=None
    def deletionAtEnd(self):
         prev=self.head
         temp=self.head.next
         while temp.next is not None:
             temp=temp.next
             prev=prev.next
         prev.next=None
    def deletionAtmid(self,pos):
        prev=self.head
        temp=temp.next
        pos=int(input("enter the pos"))
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
    def countnodes(self):
        count=0
        self.temp=self.head
        while self.temp.next is not None:
            self.temp=self.temp.next
            count=count+1
        print("THE NUMBER OF NODES : ",count)
    def search(self):
        element=int(input("enter the element"))
        self.temp=self.head
        while self.temp.next is not self.head:
            if(self.temp.data==element):
                print("the element is found")
            else:
                print("the element is not found")   
a=SLL()
a.creation()
a.display()
a.insertAtBeg()
a.display()
a.insertAtEnd()
a.display()
a.insertAtmid()
a.display()
a.deletionAtBeg()
a.display()
a.deletionAtEnd()
a.display()
a.deletionAtmid()
a.display()
a.countnodes()
a.search()