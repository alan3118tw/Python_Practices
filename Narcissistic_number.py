"""
找出水仙花數

Author: Even
Version: 0.1
"""

import math


for i in range(100,999,1):
    h = (i//100) ** 3
    t = ((i//10) % 10) ** 3
    g = (i%10) ** 3
    if(h + t + g == i):
        print(i)