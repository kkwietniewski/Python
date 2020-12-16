#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input())
result = ''
count = 0
count1 = 0
i = 0
rest = 1
while n > 0:
    rest = n % 2
    result += str(rest)
    n = math.floor(n / 2)
result = result[::-1]
for i in range(len(result)):
    # print(result[i], i, count, count1)
    if result[i] == '1':
        count +=1
        if count > count1:
            count1 = count
    elif result[i] == '0':
        count = 0
print(count1)