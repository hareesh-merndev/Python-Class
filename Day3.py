# fibonacci series
a, b = 0, 1
while a < 10:
    print(a, end=' ')
    a, b = b, a + b
# for leet
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b

# tribonacci
a, b, c = 0, 1, 1
while a < 30:
    print(a, end=' ')
    a, b, c = b, c, a + b + c

# for leet
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        a, b, c = 0, 1, 1
        
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
    
        return c
# list
# list indices
# list slicing
# list method (append,insert,remove,pop,clear,index,count,sort,reverse)
# list operations(concentratioon, repetation,membership)
# mapping(map,filter,reduce)

list=[1,2,3,4,5]
print(list[4])
# slice syntax [start index (included),end index(excluded)]
print(list[1:4])
# list operator
a=[1,2,3]
b=[4,5]
print(a+b)

# repetation operator(*)
num1=[1,2]
print(num1*3)

# membership operator(in,not-in)
fruits=["apple","banana","watermelon,""grape"]
print("apple" in fruits)
print("mango" in fruits)

# comparision opearator
list1=[1,2,3]
list2=[4,5,6]
print(list1==list2)
print(list1<list2)
print(list1>list2)

a=[1,2,3,4]
b=[5,6,7,8]
# index
print(a[3])
# slice
print(a[1:3])
# repetation
print(a*3,b*3)
# membership
print(3 in a)
print(9 in b)
# comparision
print(a==b)
print(a<b)
print(a>b)

# list methods
# append is to merge and the element at last only
num=[1,2,3]
num.append(4)
print(num)
# insert->syntax is  num.insert(position,value)
num.insert(3,2)
print(num)
# extend->
a=[1,2]
b=[3,4]
a.extend(b)
print(a)

print(num)
# pop
num=[10,12,13]
num.pop(1)
print(num)
# clear
num.clear()
print(num)
# index
num=[1,2,3,4]
print(num.index(3))#shows that present in which index
# count
print(num.count(2))

# sort
a=[1,22,3,56,79,8,90]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# reverse
a=[1,2,3,4,5,6,7,8]
a.reverse()
print(a)

# copy
a=[1,2,3]
b=a.copy()
print(b)# remove
num=[1,2,3,4,5]
num.remove(4)

# map, filter and list-->functional programming<--

num=[1,2,3,4]
# result=list(map(lambda x:x*2,num))
# print(result)
def fun(x):
    return x*2
result=list(map(fun,num))
print(result)

num1=[1,2,3,4,5,6,7,8,9,0]
resultone=list(filter(lambda x:x%2==0,num1))
print(resultone)

# convert into a single value -->functional module
from functools import reduce
num=[1,2,3,4,5]
result=reduce(lambda a,b:a+b,num)
print(result)
# seperate odd and even
num0=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda x:x%2==0,num0))
odd=list(filter(lambda x:x%2!=0,num0))
print("the even number is=",even)
print("odd number is=",odd)

# palindrome
word=input("enter a word:")
if word==word[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome")

# method 2
value = input("Enter a word or number: ")

rev = ""
for ch in value:
    rev = ch + rev

if value == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

