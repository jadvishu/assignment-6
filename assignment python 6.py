#Answer of question 1
n=int(input("Enter the number to check whether it is perfect or not:"))
def perfect_number(n):
    sum = 0
    
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(n))

#Answer of question 2

str1=input("Enter the word and see if it is palindrome ")
if str1==str1[::-1]:
    print("This word is palindrome")
else:
    print("This word is not palindrome")

#Answer of question 3
n=int(input("Enter number of rows: "))
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
        
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
    print()



#Answer of question 4
from string import ascii_lowercase as asc_lower
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])
strng=input("Enter string:")
if(check(strng)==True):
      print("The string is a pangram")
else:
      print("The string isn't a pangram")



#Answer of question 5 
st=input("Enter a hyphene separated sequence of words to sort:")
lst=st.split("-")
lst.sort()
print("Sorted sequence:")
print("-".join(lst))

#Answer of question 6
order=input("What do you want to print SID,name or class:") 
def student_data(student_id,**data):
    if order=="sid":
            print("\nStudent ID:",student_id)
    elif order=="name" or order=="class":
            print("Student name:",{data['student_name']}, "Student class:",{data['student_class']})
            print("\n")
    



student_data(21102072, student_name="Vishal Thakur", student_class="B.tech")
student_data(21102073, student_name="vicky",student_class="B.tech")
student_data(21102074, student_name="Lapata", student_class="B.tech")

#Answer of question 7
class Student:
    pass

class Marks:
    pass

name1 = Student()
fail = Marks()
print(isinstance(name1, Student))
print(isinstance(fail, Student))
print(isinstance(fail, Marks)) 
print(isinstance(name1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))

#Answer of question 8
class sumzero:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(sumzero().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))


#Answer of question 9
class validity:
    def check(self,str1):
        lst=[]
        brak={"(":")","{":"}","[":"]"}
        for i in str1:
            if i in brak:
                lst.append(i)
            elif len(lst)==0 or brak[lst.pop()]!=i:
                return False
        return len(lst)==0

print(validity().check("(){}[]"))
print(validity().check("({)}[]"))
print(validity().check("[]({}"))


