# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 15:53:04 2020

@author: yuggu
"""
def f(n,arr):
    def run(a,d):
        a[0] += d
        return a[0]
    def check(a,b):
        if a[1] or b[1]:
            
            return 1
        else:
            return 0
    # for _ in range(int(input())):
        #n = int(input())
        #arr = list(map(int,input().split()))
        #arr = arr[:3]
        # if len(set(arr)) == 1:
        #     print(1,1)
        # else:
    res = []
    d,e,f =arr[0],arr[1],arr[2]
    
    if True:
        a = [1 + arr[0],False]
        b = [2 + arr[1],False]
        c = [3 + arr[2],False]
        limit = 4
        count = 1
        a[1] = True
        while limit!= 0:
            if count >= 3:
                res.append(3)
                count = 1
                break
            if not (a[1] == True and b[1] == True):
                if a[0] == b[0]:
                    if check(a,b):
                        a[1],b[1] = True,True
                        count += 1
            if not (b[1] == True and c[1] == True):
                if b[0] == c[0]:
                    if check(b,c):
                        b[1],c[1] = True,True
                        count += 1
            if not (a[1] == True and c[1] == True):
                if a[0] == c[0]:
                    if check(a,c):
                        a[1],c[1] = True,True
                        count += 1
            a[0] = run(a,d)
            b[0] = run(b,e)
            c[0] = run(c,f)
            limit -= 1
    if len(res) == 0:
        res.append(count)
    if True:
        a = [1 + arr[0],False]
        b = [2 + arr[1],False]
        c = [3 + arr[2],False]
        limit = 4
        count = 1
        b[1] = True
        while limit!= 0:
            if count >= 3:
                res.append(3)
                count = 1
                break
            if not (a[1] == True and b[1] == True):
                if a[0] == b[0]:
                    if check(a,b):
                        a[1],b[1] = True,True
                        count += 1
            if not (b[1] == True and c[1] == True):
                if b[0] == c[0]:
                    if check(b,c):
                        b[1],c[1] = True,True
                        count += 1
            if not (a[1] == True and c[1] == True):
                if a[0] == c[0]:
                    if check(a,c):
                        a[1],c[1] = True,True
                        count += 1
            a[0] = run(a,d)
            b[0] = run(b,e)
            c[0] = run(c,f)
            limit -= 1
    if len(res) == 1:
        res.append(count)
    if True:
        a = [1 + arr[0],False]
        b = [2 + arr[1],False]
        c = [3 + arr[2],False]
        limit = 4
        count = 1
        c[1] = True
        while limit!= 0:
            if count >= 3:
                res.append(3)
                count = 1
                break
            if not (a[1] == True and b[1] == True):
                if a[0] == b[0]:
                    if check(a,b):
                        a[1],b[1] = True,True
                        count += 1
            if not (b[1] == True and c[1] == True):
                if b[0] == c[0]:
                    if check(b,c):
                        b[1],c[1] = True,True
                        count += 1
            if not (a[1] == True and c[1] == True):
                if a[0] == c[0]:
                    if check(a,c):
                        a[1],c[1] = True,True
                        count += 1
            a[0] = run(a,d)
            b[0] = run(b,e)
            c[0] = run(c,f)
            limit -= 1
    if len(res) == 2:
        res.append(count)
    print(arr)
    print(min(res),max(res))
    #print(res)
        
inputs = [('0', '0', '0'), ('0', '0', '1'), ('0', '0', '2'), ('0', '0', '3'), ('0', '0', '4'), ('0', '0', '5'), ('0', '1', '0'), ('0', '1', '1'), ('0', '1', '2'), ('0', '1', '3'), ('0', '1', '4'), ('0', '1', '5'), ('0', '2', '0'), ('0', '2', '1'), ('0', '2', '2'), ('0', '2', '3'), ('0', '2', '4'), ('0', '2', '5'), ('0', '3', '0'), ('0', '3', '1'), ('0', '3', '2'), ('0', '3', '3'), ('0', '3', '4'), ('0', '3', '5'), ('0', '4', '0'), ('0', '4', '1'), ('0', '4', '2'), ('0', '4', '3'), ('0', '4', '4'), ('0', '4', '5'), ('0', '5', '0'), ('0', '5', '1'), ('0', '5', '2'), ('0', '5', '3'), ('0', '5', '4'), ('0', '5', '5'), ('1', '0', '0'), ('1', '0', '1'), ('1', '0', '2'), ('1', '0', '3'), ('1', '0', '4'), ('1', '0', '5'), ('1', '1', '0'), ('1', '1', '1'), ('1', '1', '2'), ('1', '1', '3'), ('1', '1', '4'), ('1', '1', '5'), ('1', '2', '0'), ('1', '2', '1'), ('1', '2', '2'), ('1', '2', '3'), ('1', '2', '4'), ('1', '2', '5'), ('1', '3', '0'), ('1', '3', '1'), ('1', '3', '2'), ('1', '3', '3'), ('1', '3', '4'), ('1', '3', '5'), ('1', '4', '0'), ('1', '4', '1'), ('1', '4', '2'), ('1', '4', '3'), ('1', '4', '4'), ('1', '4', '5'), ('1', '5', '0'), ('1', '5', '1'), ('1', '5', '2'), ('1', '5', '3'), ('1', '5', '4'), ('1', '5', '5'), ('2', '0', '0'), ('2', '0', '1'), ('2', '0', '2'), ('2', '0', '3'), ('2', '0', '4'), ('2', '0', '5'), ('2', '1', '0'), ('2', '1', '1'), ('2', '1', '2'), ('2', '1', '3'), ('2', '1', '4'), ('2', '1', '5'), ('2', '2', '0'), ('2', '2', '1'), ('2', '2', '2'), ('2', '2', '3'), ('2', '2', '4'), ('2', '2', '5'), ('2', '3', '0'), ('2', '3', '1'), ('2', '3', '2'), ('2', '3', '3'), ('2', '3', '4'), ('2', '3', '5'), ('2', '4', '0'), ('2', '4', '1'), ('2', '4', '2'), ('2', '4', '3'), ('2', '4', '4'), ('2', '4', '5'), ('2', '5', '0'), ('2', '5', '1'), ('2', '5', '2'), ('2', '5', '3'), ('2', '5', '4'), ('2', '5', '5'), ('3', '0', '0'), ('3', '0', '1'), ('3', '0', '2'), ('3', '0', '3'), ('3', '0', '4'), ('3', '0', '5'), ('3', '1', '0'), ('3', '1', '1'), ('3', '1', '2'), ('3', '1', '3'), ('3', '1', '4'), ('3', '1', '5'), ('3', '2', '0'), ('3', '2', '1'), ('3', '2', '2'), ('3', '2', '3'), ('3', '2', '4'), ('3', '2', '5'), ('3', '3', '0'), ('3', '3', '1'), ('3', '3', '2'), ('3', '3', '3'), ('3', '3', '4'), ('3', '3', '5'), ('3', '4', '0'), ('3', '4', '1'), ('3', '4', '2'), ('3', '4', '3'), ('3', '4', '4'), ('3', '4', '5'), ('3', '5', '0'), ('3', '5', '1'), ('3', '5', '2'), ('3', '5', '3'), ('3', '5', '4'), ('3', '5', '5'), ('4', '0', '0'), ('4', '0', '1'), ('4', '0', '2'), ('4', '0', '3'), ('4', '0', '4'), ('4', '0', '5'), ('4', '1', '0'), ('4', '1', '1'), ('4', '1', '2'), ('4', '1', '3'), ('4', '1', '4'), ('4', '1', '5'), ('4', '2', '0'), ('4', '2', '1'), ('4', '2', '2'), ('4', '2', '3'), ('4', '2', '4'), ('4', '2', '5'), ('4', '3', '0'), ('4', '3', '1'), ('4', '3', '2'), ('4', '3', '3'), ('4', '3', '4'), ('4', '3', '5'), ('4', '4', '0'), ('4', '4', '1'), ('4', '4', '2'), ('4', '4', '3'), ('4', '4', '4'), ('4', '4', '5'), ('4', '5', '0'), ('4', '5', '1'), ('4', '5', '2'), ('4', '5', '3'), ('4', '5', '4'), ('4', '5', '5'), ('5', '0', '0'), ('5', '0', '1'), ('5', '0', '2'), ('5', '0', '3'), ('5', '0', '4'), ('5', '0', '5'), ('5', '1', '0'), ('5', '1', '1'), ('5', '1', '2'), ('5', '1', '3'), ('5', '1', '4'), ('5', '1', '5'), ('5', '2', '0'), ('5', '2', '1'), ('5', '2', '2'), ('5', '2', '3'), ('5', '2', '4'), ('5', '2', '5'), ('5', '3', '0'), ('5', '3', '1'), ('5', '3', '2'), ('5', '3', '3'), ('5', '3', '4'), ('5', '3', '5'), ('5', '4', '0'), ('5', '4', '1'), ('5', '4', '2'), ('5', '4', '3'), ('5', '4', '4'), ('5', '4', '5'), ('5', '5', '0'), ('5', '5', '1'), ('5', '5', '2'), ('5', '5', '3'), ('5', '5', '4'), ('5', '5', '5')]
for i in inputs:
    i = list(i)
    i = list(map(int,i))
    f(3,i)