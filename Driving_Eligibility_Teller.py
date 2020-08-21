import os
os.system("cls")
name=input("Enter your name : ")
age=int(input("Enter your age : "))
if (age>18):
    print(name,"can drive")
elif (age<18):
    print(name,"cannot drive")    
else:
    print(name,"give a driving test")