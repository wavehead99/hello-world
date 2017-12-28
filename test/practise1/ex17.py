'''
Created on 28 Dec 2017

@author: epatdal
'''
#from sys import argv
#Sfrom os.path import exists

filepath="C:\\tmp\\"

print ("this is the filepath",filepath)

fromfilename=filepath+"pythontest.txt"
tofilename=filepath+"copypythontest.txt"

fromfr=open(fromfilename)

tofile=open(tofilename,'w')

data=fromfr.read()

totallength=len(data)

tofile.write(data)

tofile.close()
fromfr.close()

print ("all allright this is now done", totallength)


