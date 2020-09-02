# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 16:02:05 2020

@author: 91842
"""
from math import floor
m = int(input())
count1 = 0;count2=0;count3=0
if m>=10:
    count1 = floor(m/10)
    m=m%10
        
    
if m>=5 and m<10:
      count2 = 1
      m=m-5
        
        
        
if m>=1 and m<5:
    count3 = m
    
ans = count1+count2+count3
print(ans)
        
        