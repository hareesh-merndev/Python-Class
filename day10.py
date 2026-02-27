# linked list

# advantages
# 1) stored in memory
# 2) fast access by index
# 3) must traverse step by step
# 4) flexible size

# BASIC STRUCTURE
# datas and address of the next node

# step by step logic

# create a class node
# store data
# store reference to next node

# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# n1=node(10)
# n2=node(20)
# n3=node(30)
# n1.next=n2
# n2.next=n3
# print(n1.data)
# print(n1.next.data)

# create linkedlist class
# create head pointer
# head store first node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def insert_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

li = LinkedList()

li.insert_begin(10)
li.insert_begin(5)
li.insert_begin(20)
li.insert_begin(30)
li.insert_end(50)

li.display()