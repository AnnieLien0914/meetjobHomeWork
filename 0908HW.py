# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:40:04 2022

@author: Fang" Yu
"""

"""

費氏數列:一連串的數字

#用串列的方式呈現

第一題:請利用費氏數列 算出前25 項的總和
1 1 2 3 5 8 13 ...

第二題:請利用費氏數列 算出 2/1, 3/2, 5/3, 8/5, 13/8 前25項總和

有空可做"
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

print("-"*5,"第一題","-"*5)
print()

arr = []

for i in range(1,26):
    if i == 1:
        a = 1
        arr = [0,1]
    else:
        a = arr[0]+arr[1]
        del arr[0]
        arr.append(a)
    print(a, end=',')

print()    
print("總和為:",sum(arr))

print()
print("-"*5,"第二題","-"*5)
print()

arr2 = []
for x in range(2,27):
    if x == 2:
        a2 = 2
        arr2 = [1,2]
    else:
        a2 = arr2[0]+arr2[1] 
        del arr2[0]
        arr2.append(a2)
        
    print(a2,"/", arr2[0], end=",")    
    y = []
    y2 = (arr2[1] / arr2[0])
    y.append(y2)
print()   
print("總和為:",sum(y))


print()
print("-"*5,"有空題","-"*5)
print()

arr3=[]
for z in range(1,16):
    arr3.append(z)
print(arr3)
print()

for g in range(1,6):
    
    for f in range(g):
        n = 0 + f
        print(arr3[0],end=" ")
        del arr3[0]
        
    print()
