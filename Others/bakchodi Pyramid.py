# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:26:25 2020

@author: yuggu
"""

n = int(input())
m = n
for i in range(n):
    for j in range(n):
        if j == m-1:
            print(i+1,end = '')
        else:
            print('0',end='')
    print('\n')
    m = m-1
