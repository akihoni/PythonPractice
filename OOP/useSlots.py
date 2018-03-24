'''
Created on 2018年3月24日

@author: akiho
'''
class Person(object):
    __slots__ = ('name', 'age')

class Student(Person):
    __slots__ = ()
    
s = Student()
s.name = 'Amy'
s.age = 9
print('name is', s.name)
print('age is', s.age)
# s.score = 99