"""
Question:Class練習
Author:Even
Last Update:2019.10.5
"""
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def introduce_myself(self):
        print('My name is %s. %d years old. Salary is %d a month.'%(self.name,self.age,self.salary))

if __name__ == "__main__":
    E1=Employee('GG',37,35000)
    E1.introduce_myself()
