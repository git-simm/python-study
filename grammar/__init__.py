#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import grammar.Employee
# 导入某一个类的写法
from grammar.Employee import Employee

if __name__ == "__main__":
    "创建 Employee 类的第一个对象"
    emp1 = Employee("Zara", 2000)
    "创建 Employee 类的第二个对象"
    emp2 = Employee("Manni", 5000)
    emp1.displayEmployee()
    emp2.displayEmployee()
    print("Total Employee %d" % Employee.empCount)

    if True:
        print(1);
    else:
        print(2);
