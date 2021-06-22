###
# sorting list
###

lst= ["Mango", "PineApple", "Orange", "Apple"]
#method 1 
lst.sort()
print(lst) # ['Apple', 'Mango', 'Orange', 'PineApple']
#method 2 generic sorting
new_lst = sorted(lst)
print(new_lst) # ['Apple', 'Mango', 'Orange', 'PineApple']
#reverse sorting
new_lst = sorted(lst, reverse=True)
print(new_lst)# ['PineApple', 'Orange', 'Mango', 'Apple']

###
# sorting dictionary
###

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#method 1
new_dict = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
print(new_dict) # {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
#method 2
new_dict = dict(sorted(d.items(), key=lambda item: item[1]))
print(new_dict) # {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}

###
# Print on the Same Line
###

#method 1
print("I'm a Python", end=" ")
print("Programmer")
#method 2
import sys
sys.stdout.write("I'm a Python")
sys.stdout.write(" Programmer")

###
# Merge Two Dictionaries
###
def merge_two_dict(x, y):
    z = x.copy()
    z.update(y)
    return z
x = {"A" : 1, "B" : 2}
y = {"C" : 3, "D" : 4}
merge_two_dict(x, y) # {'A': 1, 'B': 2, 'C': 3, 'D': 4}

###
#  Reverse
###
def reverse(data):
    return data[::-1]
reverse("Python") #nohtyP
reverse("23354") #45332

###
# Check duplicates
###
def check_duplicates(lst):
    return len(lst) != len(set(lst))
lst1 = [1, 2, 3, 3]
lst2 = [1, 2, 3]
print(check_duplicates(lst1)) # True

###
# Filter unique
###
mylist = [1, 2, 3, 2, 5, 6, 6, 5, 7]
unique = list(set(mylist))
print(unique) #[1, 2, 3, 5, 6, 7]

print(check_duplicates(lst2)) # False


###
# digitize / split a number in the list of the digits.
###
def Digitize(num):
  return list(map(int,str(num)))
print(Digitize(321)) # [3, 2, 1]
print(Digitize(900)) # [9, 0, 0]

##
# Byte syze
##
def byte_size(string):
  return len(string.encode('utf-8'))
byte_size("hello") # 5
byte_size("Python Programming") #18


###
# Similarity
###
def similarity(x, y):
    return [item for item in x if item in y]
x = [1, 2, 3, 4, 5]
y = [1, 2, 3]
similarity(x,y) #[1, 2, 3]


###
# Memory usage
###
import sys
var1 = 500
var2 = "Python"
print(sys.getsizeof(var1)) # 28


###
# Get Vowels
### 
def GetVowels(string):
    return [item for item in string if item in 'aeiou']
print(GetVowels("asert")) # ['a', 'e']
print(GetVowels("football")) # ['o', 'o', 'a']

###
# Check Palindrome
### 
def palindrome(string):
    return string == string[::-1]
print(palindrome('mom')) # True
print(palindrome('bob')) # True
print(palindrome('desk')) # False

###
# Fast way of Swap
### 
#old method
a = 5
b = 6
temp = a
a = b
b = temp 
print(a, b) # 6 5
#new and fast method
a = 5
b = 6
a, b = b, a
print(a, b) # 6 5

###
# Shuffle
### 
import random
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst) # [1, 2, 3, 5, 4]
random.shuffle(lst)
print(lst) # [4, 2, 5, 3, 1]

###
# Error Handling
### 
try:
    print(a) # a not defined error occur
except:
    print(b) # b not defined again error
else: 
    print("Program is still running, Error is handled")

###
# Make First letter Bigger
###  
string1 = "python programming language"
print(string1.title()) # Python Programming Language
string2 = "learn python"
print(string2.title()) # Learn Python

###
# Get Head and Tail of List
### 
def head(lst):
    return lst[0]
def tail(lst):
    return lst[len(lst) - 1]
lst = [1, 2, 3, 4, 5]
print(head(lst)) # 1
print(tail(lst)) # 5

###
# Prime Checking
### 

import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
print(is_prime(11)) # True
print(is_prime(4)) # False


###
# Convert to Binary
### 
def convertToBinary(num):
    return bin(num)
print(convertToBinary(900)) # 0b1110000100
print(convertToBinary(300)) # 0b100101100

###
# Convert Words to List
### 
import re
def WordToList(string, pattern = '[a-zA-Z-]+'):
  return re.findall(pattern, string)
print(WordToList("Python")) #['Python']
print(WordToList("Are you a Programmer?")) # ['Are', 'you', 'a', 'Programmer']

###
#
### 
