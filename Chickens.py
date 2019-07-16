"""
百錢百雞問題
公雞一隻5元，母雞一隻3元，小雞三隻1元

Author: Even
Version:0.1
Last Update: 2019/07/16
"""
for num_cock in range(0,20):     #公雞最多20隻
    for num_hen in range (0,33):     #母雞最多33隻
        remain = 100 - num_cock - num_hen
        if (num_cock*5) + (num_hen*3) + (remain/3) == 100:
            print('公雞 : %d隻，母雞 : %d隻，小雞 : %d隻' %(num_cock,num_hen,remain))
