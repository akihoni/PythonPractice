'''
Created on 2018年3月23日

@author: akiho
'''
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b) #将n-1个盘子从a移到b
        move(1, a, b, c) #�将最后一个盘子从a移到c
        move(n-1, b, a, c) #将n-1个盘子从b移到c
    
move(3, 'A', 'B', 'C')