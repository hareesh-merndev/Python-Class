# priority queue
# remove elements based on elements/priority instead of order

# higher priority removes first
# not normal fifo
#  smaller number=higher priority

# task-1
# task-2
# task-3

# real-time example:
# hospital emergency room
# cpu task scheduling
# printer task priority
# network packet routing

# normal queue vs priority queue

# heap
# smallest number = highest priority
# automatic sorting
# uses heaping modules

# pseudo Code 
# insert
# import heapq
# create empty priority queue - create empty list
# insert element with priority
# heap arranges automatically

# remove
# remove smallest priority element

# import heapq

# pq=[]

# heapq.heappush(pq,3)

# heapq.heappush(pq,2)

# heapq.heappush(pq,1)

# print("priority queue",pq)

# print("removed",heapq.heappop(pq))

# print("removed",heapq.heappop(pq))

# print("removed",heapq.heappop(pq))
# 83.remove duplicated from sorted list

# def remove_duplicates(num):
#     if not num:
#         return []
#     result = [num[0]]
#     for i in range(1, len(num)):
#         if num[i] != num[i - 1]:
#             result.append(num[i])
#     return result
# print(remove_duplicates([1,1,2,2,3,4,4]))

# # 557. Reverse Words in a String III
# def reverse_words(s):
#     words = s.split(" ")
#     reversed_words = [word[::-1] for word in words]
#     return " ".join(reversed_words)
# s = "hareesh"
# print(reverse_words(s))

