"""
Calculate the area of a circle

Author: Even
Version: 0.1
Last update: 2019/7/7
"""


import math


radius = float(input('Please input a number as radius of circle: '))
area = float((radius ** 2) * math.pi)
print('Area of circle is  %.2f''' % area)