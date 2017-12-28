'''
Created on 28 Dec 2017

@author: epatdal
'''

def add (a,b):
    print ("add a to b")
    return a + b

def subtract(a,b):
    return a - b

x=add(10,100)
y=subtract(100,10)
z=add(10,subtract(90,80))

print (x,y,z)




