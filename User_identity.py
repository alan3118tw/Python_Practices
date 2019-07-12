"""
使用者識別
default user name: Even
default user password: 3333

Author: Even
Version: 0.1
"""


user_name = input('Please input the user name:' )
user_password = input('Please input the user password: ')
if user_name == 'Even' and user_password == '3333' :
    print('Pass')
else :
    print('failed')