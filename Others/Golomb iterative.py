# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 21:54:40 2020

@author: yuggu
"""


def printGolombSequence(K,N): 
    MAX = 100001
  
    # Initialise the array 
    arr = [0] * MAX
  
    # Initialise the cnt to 0 
    cnt = 0
  
    # First and second element 
    # of Golomb Sequence is 0, 1 
    arr[0] = 0
    arr[1] = 1
  
    # Map to store the count of 
    # current element in Golomb 
    # Sequence 
    M = dict() 
  
    # Store the count of 2 
    M[2] = 2
  
    # Iterate over 2 to N 
    for i in range(2, N + 1): 
  
        # If cnt is equals to 0 
        # then we have new number 
        # for Golomb Sequence 
        # which is 1 + previous 
        # element 
        if (cnt == 0): 
            arr[i] = 1 + arr[i - 1] 
            cnt = M[arr[i]] 
            cnt -= 1
  
        # Else the current element 
        # is the previous element 
        # in this Sequence 
        else: 
            arr[i] = arr[i - 1] 
            cnt -= 1
  
        # Map the current index to 
        # current value in arr[] 
        M[i] = arr[i] 
        result = []
        
        for i in range(K, N + 1): 
            result.append(arr[i])
            
    return result



T = int(input())
while T:
    n,k = map(int,input().split())
    s = 0
    a = printGolombSequence(n,k)
    for i in a:
       s += i**2 
    s = s% ((10**9)+7)
    print(s)
    
    T -= 1
            
    
        

        
        
    
  