# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:42:12 2024

@author: 88697
"""
number = float(input('請輸入數字 = '))

if number % 2 == 0:
    print('該數是偶數')
else:
    if (number+1) % 2 == 0:
       print('該數是奇數')
    else:
       print('該數不是整數')
