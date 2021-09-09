#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 19:04:52 2021

@author: bocuin
@source : belajarpython.com | w3school.com/python
@tag : #belajar_python dasar
"""

#while loop
count = 5
while (count < 9 ):
    print ("the count is : ", count)
    count = count + 1
    
print ("good bye")

#for loop
angka = [1, 2, 3, 4, 5]
for x in angka:
    print(x)
    
#contoh for loop
buah = ["nanas", "apel", "jeruk"]
for makanan in buah:
    print ("saya suka makan buah", makanan)
    
#nested loop example
i = 2 
while(1 < 100):
    j = 2
    while(j <=(i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print(i,"is prime")
    i = i + 1
    
print("good bye")

#string 
#string update
pesan = 'hello world'
print ("update string:- ",pesan[:6]+'python')

#operation string format
print ("My name is %s and weight is %d kg!" % ('Zara', 21)) 

#tree quote 
kutip_tiga = """hai semua apa kabar"""
print(kutip_tiga)

#list
list1 = ['kimia', 'fisika', 1993, 2017]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

#acces value on the list
print(list1[0])
print(list2[0:5])
print(list3[0:3])

#update value on list 
list = ['kimia', 'fisika', 1993, 2017]
print ("there value in index 2: ", list[2])

list[2] = 2001
print ("update new value in index 2 : ", list[2])

#delete value in list
list = ['kimia', 'fisika', 1993, 2017]

print(list)
del list[2]
print ("after delete value in index 2: ",list)

#basic operation list in python
""""
Python Expression 	       Hasil 	            Penjelasan
len([1, 2, 3, 4]) 	        4 	                 Length
[1, 2, 3] + [4, 5, 6] 	   [1, 2, 3, 4, 5, 6] 	 Concatenation
['Halo!'] * 2 	           ['Halo!', 'Halo!'] 	 Repetition
2 in [1, 2, 3] 	           True 	             Membership
for x in [1,2,3] :
    print (x,end = ' ')    1 2 3 	             Iteration
"""

#tuple
tup1 = ('kimia', 'fisika', 1993, 2017)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

"""Untuk menulis tupel yang berisi satu nilai,
Anda harus memasukkan koma, meskipun hanya ada satu nilai,
contohnya : tup1 = (50,)"""

#acess value in tuple
tup1 = ('kimia', 'fisika', 1993, 2017)
tup2 = (1, 2, 3, 4, 5)

print("tup1[0:3]", tup1[0:3])
print("tup2[0:4] ",tup2[0:4])

#update value in tuple 
tup1 = ( 12, 12.34 )
tup2 = ('abc', 'xyz')

tup3 = tup1 + tup2
print(tup3)

#delete value on tuple
tup1 = ('kimia', 'fisika', 1993, 2017)
print ("before delete tuple: ", tup1)

    #delete tup statement with del 
del tup1
tup1 = ('bahasa', 'math', 2020)
print("after delete tuple: ", tup1)

#dictionary
#acces  in dictionary

dict = {'name':'zara', 'age': 7, 'class': 'first'}
print ("dict['name']: ", dict['name'])
print ("dict['age']: ", dict['age'])

#update dictionary value 
dict = {'name':'zara', 'age': 7, 'class': 'first'}
dict['age'] = 8 #mengubah entri yang sudah ada(yang dirubah entri 'age')
dict['school'] = 'smkn 10' #menambah entri baru

print ("dict['age]: ",dict['age'])
print ("dict['school']: ", dict['school'])

#delete dictionary 
dict = {'name':'zara', 'age': 7, 'class': 'first'}

del dict ['name'] #hapus entri dengan key 'name'
dict.clear() #hapus semua entri di dict
del dict #hapus dict yang sudah ada

print("dict['age']: ", dict['age'])
print ("dict['school']: ", dict['school'])

#date-time 

import time;
ticks = time.time()
print("sekarang jam:", ticks)

#get time now
import time;
localtime = time.localtime(time.time())
print ("waktu local saat ini:", localtime)

#Get Time formatted
import time;

localtime = time.asctime( time.localtime(time.time()))
print ("waktu lokal saat ini:", localtime)

#get calenear for 1 month
import calendar

cal = calendar.month(2021, 9) #2021 adalah tahun dan 9 adalah bulannya
print("dibawah ini kalendernya:")
print(cal)

#function 
def printme( str ):
    "this is a passed string into this function"
    print(str)
    return

def my_function():
    print("hello from function")
    
my_function()

#module 
def print_func( par ):
    print( "hallo : ", par)
    return

#import module support
#untuk mengimpor modul hello.py, Anda perlu meletakkan perintah berikut di bagian atas script.
import support

#anda bisa memanggil fungsi defined sebagai berikut
support.print_func("andy")

#import mymodule
#buat file baru dengan nama 'mymodule1.py' dan  isikan  kode dibawah
person1 = {
    "name": "john",
    "age":36,
    "country":"indonesia"
}     
#kemudian save dan kembali ke kodingan yang sebelmunya
import mymodule1

a = mymodule1.person1["age"]
print(a)                    

#naming mymodule1
import mymodule1 as mx

a = mymodule1.person1["age"]
print(a)                    

#There are several built-in modules in Python, which you can import whenever you like.
import platform

x = platform.system()
print(x)


#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
import platform

x = dir(platform)
print(x) #e dir() function can be used on all modules, also the ones you create yourself.


#import form module 
#You can choose to import only parts from a module, by using the from keyword
#example The module named mymodule has one function and one dictionary:

from mymodule1 import person1

print (person1["age"])

#input and output
x = input("ketik sesuatu: ")
print("hasilnya: ",x)

#json
#Convert a Python object containing all the legal data types:
 import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

#simple json
import json

#some json:
x = '{ "name":"john", "age":33, "city":"semarang"}'

#parse x:
y = json.loads(x)

#the result is a python dictionary:
print(y["name"])

#class

#create simple class
#Create a class named Person, use the __init__() function to assign values for name and age:
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = person("john", 36)

print(p1.name)
print(p1.age)

#object method
#insert a function that prints a greeting, and execute it on the p1 object
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("hello my name is " + self.name)
        
p1 = person("john", 33)
p1.myfunc()

#example again :)
class employee:
    'common base class for all employees'
    empcount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        employee.empcount += 1
        
    def displaycount(self):
        print ("total employees %d" %employee.empcount)
        
    def displayemployee(self):
        print ("name :", self.name, ", salary: ", self.salary)
        
#membuat instance objects
#Untuk membuat instances kelas, Anda memanggil class menggunakan nama class dan meneruskan argumen apa pun yang metode init terima.
class employed:
    'common base class for all employed'
    empcount = 0
   
    def __init__(self, name, salary):
       self.name = name
       self.salary = salary
       employed.empcount += 1
       
    def displaycount(self):
       print("total employed %d" % employed.empcount)
       
    def displayemployed(self):
       print ("name: ", self.name, ",salary: ",self.salary)
       
#this is would create first object og employed class
emp1 = employed("zara",2000)
#this is would create second objectof employed class
emp2 = employed("mani", 5000)
emp1.displayemployed()
emp2.displayemployed()
print ("total employed %d" %employed.empcount)
