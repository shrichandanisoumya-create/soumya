import string


CHAPTER 1 - INTRODUCTION TO PYTHON


types in python
#1. integer -ve_0_+ve
#2. float 3.44..... point wale
#3. boolean True/False
#4. string - "hello" 'hello' """hello"""
#5. none - None

keywords in python
# reserved words
# and, 
# as, 
# assert, 
#   break,
#  class, 
# continue,
#  def,
#  del,
#  elif,
#  else,
#  except,
#  False,
#  finally,
#  for,
#  from,
#  global,
#  if,
#  import,
#  in,
#  is,
#  lambda,
#  None, 
# nonlocal,
#  not, 
# or,
#  pass,
#  raise, 
# return,
#  True,
#  try,
#  while,
#  with,
#  yield
Operators- +,-,*,/,%,//,** etc...
#a%b to find reminder
#! not equal to
# <=,>= greater ,less than
#logical operators - and, or, not
# and operator tab use karte hai jab 2 value par kaam karna ho
# or give yaa
Type of variable
# to find type of variable use type()
# to convert one type to another use int(), float(), str(), bool()
input in python
# to take input from user use input() function
# eg. input("Enter your name: ")
#result of input() is always string, so we need to convert it to required type using type conversion functions
CHAPTER 2 -STRINGS AND CONDITIONAL STATEMENTS
#string is an datatype it store text in it
#eg. name = "John"
escape sequence - \n, \t, \\, \', \", \r, \b, \f
#\n - new line
#\t - tab
#\\ - backslash
#\' - single quote
#\" - double quote
#\r - carriage return
#\b - backspace
#\f - form feed
#contracting string - "Hello" + "World" = "HelloWorld"
#length of string - len()
indexing in string - 0,1,2,3,4,5,6,7,8,9
#accessing string using index - name[0], name[1], name[-1] etc
#indexing- number of characters in string
#to take characters between 2 index use slicing - name[0:5], name[1:4], name[-5:-1] etc
#slicing in string - name[0:5], name[1:4], name[-5:-1] etc
length of string - len()
#gives length of string
#---------> positive indexing - 0,1,2,3,4,5,6,7,8,9
#<--------- negative indexing - -1,-2,-3,-4,-5,-6,-7,-8,-9
Functions in python
#for eg-
#str1='i am learning python'
#str1.upper() - converts string to uppercase
#str1.lower() - converts string to lowercase
#str1.strip() - removes whitespace from beginning and end
#str1.replace('old value', 'new value') - replaces 'old value' with 'new value'
#print(str1.endswith('python')) returns True if string ends with 'python', else False
#str1.capitalize() - capitalizes first letter of string
#str1.count('a') - counts number of occurrences of 'a' in string
#vs code sujjests functions when we type str1. and then press tab so no need to remember all functions
conditional statements in python
#if(condition)
#elif(condition)
#else- if the condition is not true
lists in python
#list is a collection of items in a particular order
# eg. mylist = [1, 2, 3, 4, 5]
#               0  1  2  3  4
#              -5 -4 -3 -2 -1          
#string is immutable but list is mutable
#list.append() - adds an item to the end of the list
#list.sort() - sorts the list in ascending order
#list.sort(reverse=True) - sorts the list in descending order
#list.reverse() - reverses the order of the list
#list.insert(index, item) - inserts an item at a specified index
#list.remove(item) - removes the first occurrence of an item from the list
#list.pop(index) - removes and returns the item at a specified index
tupple in python
#a built in data type that lets you store multiple items and its immutable
#chota bhai of list just immutable
#eg. mytuple = (1, 2, 3, 4, 5)
#               0  1  2  3  4
#              -5 -4 -3 -2 -1
difference between list and tupple
#list= [1, 2, 3, 4, 5] box brackets
#tuple= (1, 2, 3, 4, 5) curly brackets
