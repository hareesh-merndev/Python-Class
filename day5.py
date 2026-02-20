# class Solution:
#     def containsDuplicate(self, nums):
#         return len(nums) != len(set(nums))
# solution = Solution()
# nums = list(map(int, input("Enter numbers separated by space: ").split()))
# result = solution.containsDuplicate(nums)
# print("Contains duplicate:", result)


###oops

# def func(a,b):
#     return a+b
# result=func(5,8)
# print(result)

# class student:
#     def details(self,name,marks):
#         if marks>40:
#             result="pass"
#             print(result)
#             print(name,marks)
#         else:
#             print("fail")
# s1=student()
# s2=student()
# s1.details("rvs,88")
            
            
# ##syntax
# class ClassName:
#     def method_name(self):
#         print("message")

class Student:
    def __init__(self,name,marks):
        self.marks=marks
    def show_result(self):
        if self.marks>=40:
            result ="pass"
        else:
            result="fail"
        print("\n student name:",self.name)
        print("Marks",self.marks)
        print("result",result)
name=input("enter name:")
marks=int(input("enter marks:"))
s1=Student(name,marks)
s1.show_result()