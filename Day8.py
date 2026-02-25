# print("Pizza Categories")
# print("1.Normal")
# print("2.Delux")
# category = int(input("Enter your Choice [1 or 2]: "))

# print("\nPizza Types")
# print("1.Veg")
# print("2.Non Veg")
# ptype = int(input("Enter your Choice [1 or 2]: "))

# if category == 1 and ptype == 1:
#     base_price = 300.0
# elif category == 1 and ptype == 2:
#     base_price = 400.0
# elif category == 2 and ptype == 1:
#     base_price = 500.0
# elif category == 2 and ptype == 2:
#     base_price = 600.0
# else:
#     base_price = 0.0

# cheese = int(input("\nEnter Cheese? [1.Yes or 2.NO]: "))
# extra_cheese = 100.0 if cheese == 1 else 0.0

# topping = int(input("Enter Topping? [1.Yes or 2.NO]: "))
# extra_topping = 100.0 if topping == 1 else 0.0

# water = int(input("Do you want Water Bottles? [1.Yes or 2.NO]: "))
# water_cost = 0.0
# if water == 1:
#     count = int(input("How many bottles?: "))
#     water_cost = count * 20.0

# ketchup = int(input("Do you want Ketchup? [1.Yes or 2.NO]: "))
# ketchup_cost = 0.0
# if ketchup == 1:
#     count = int(input("How many Packets?: "))
#     ketchup_cost = count * 5.0

# soft = int(input("Do you want Soft Drinks? [1.Yes or 2.NO]: "))
# soft_cost = 0.0
# if soft == 1:
#     count = int(input("How many Cans?: "))
#     soft_cost = count * 75.0

# takeaway = int(input("Is it a Take Away? [1.Yes or 2.NO]: "))
# takeaway_cost = 20.0 if takeaway == 1 else 0.0

# total_cost = base_price + extra_cheese + extra_topping + water_cost + ketchup_cost + soft_cost + takeaway_cost
# gst = total_cost * 0.18
# net_amount = total_cost + gst

# print("\n------------------------------------------")
# print("** Pizza Bill Generator **")
# print("------------------------------------------")
# print(f"Base Price        = {base_price}")
# print(f"Extra Cheese      = {extra_cheese}")
# print(f"Extra Toppings    = {extra_topping}")
# print(f"Water Bottle      = {water_cost}")
# print(f"Ketchup Packets   = {ketchup_cost}")
# print(f"Soft Drinks       = {soft_cost}")
# print(f"Take Away Charges = {takeaway_cost}")
# print("------------------------------------------")
# print(f"Total Cost        = {total_cost}")
# print(f"GST Charges       = {gst:.1f}")
# print("------------------------------------------")
# print(f"Net Amount Payable = {net_amount:.1f}")
# print("------------------------------------------")



# code

# stack=[]

# while True:
#     print("\n1.push 2.pop 3.peek 4.display 5.exit")
#     choice=int(input("enter choice"))
#     if choice==1:
#         val=int(input("enter value"))
#         stack.append(val)
#         print("pushed",val)
#     elif choice==2:
#         if not stack:
#             print("stack empty")
#         else:
#             print("poped",stack.pop())
#     elif choice==3:
#         if not stack:
#             print("stack empty")
#         else:
#             print("Top")
    
#     elif choice==4:
#         if not stack:
#             print("stack empty")
#         else:
#             print("Top")
#     elif choice==4:
#         print("stack",stack)
#     else:
#         print("invalid choice")


# queue operations

# enqueue--> add an item at rear
# dequeue--> remove an item from front
# front/peek--> view first item
# isempty
# size

# queue=[]
# while True:
#     print("\n1.enqueue 2.dequeue 3.peek 4.display 5.exit")
#     choice=int(input("enter choice"))
#     if choice==1:
#         val=int(input("enter value"))
#         queue.append(val)
#         print("added",val)
#     elif choice==2:
#         if not queue:
#             print("queue empty")
#         else:
#             print("removed",queue.pop())
#     elif choice==3:
#         if not queue:
#             print("queue empty")
#         else:
#             print("front:",queue[0])   
#     elif choice==4:
#         print("queue",queue)
#     elif choice==5:
#         break
#     else:
#         print("invalid choice") 


# circular queue
# 1) reuse empty spaces
# save memory

# if front is free,rear can reuse it

# n=3
# queue=[None]*3
# front=0
# rear=0

# # insert
# queue[rear]=10
# rear=(rear+1)%size




# dqnueue
# if queue full - print "queue full"
# if first element - set front =0
# move rear circularly
# insert element

# dequeue

# if queue empty - print "queue empty"
# remove first element
# if last element removed - reset front & rear


        
size = 5
queue = [None] * size
front = -1
rear = -1

def enqueue(value):
    global front, rear
    
    if (rear + 1) % size == front:
        print("Queue Full")
        return
    
    if front == -1:
        front = 0
    
    rear = (rear + 1) % size
    queue[rear] = value
    print(value, "inserted")

def dequeue():
    global front, rear
    
    if front == -1:
        print("Queue Empty")
        return
    
    removed = queue[front]
    
    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size
    
    print(removed, "removed")

def display():
    if front == -1:
        print("Queue Empty")
        return
    
    i = front
    print("Queue elements:")
    
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % size
    print()

while True:
    print("\n1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        enqueue(value)

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")