"""
找尋1~9999間的完美數

Author: Even
Version: 0.1
"""
import math


for number in range(1,10000):
    i = int(math.sqrt(number) + 1)
    sum = 0
    for i in range(1,i):
        if(number % i == 0 and number != i):
            sum = sum + i
            if i > 1 and (number/i) != i:
                sum = sum + (number / i)
    if(sum == number):
        print(number)