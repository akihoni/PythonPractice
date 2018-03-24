'''
Created on 2018年3月23日

@author: akiho
'''
def findMinAndMax(L):
    if L == []:
        return(None, None)
    Max = L[0]
    Min = L[0]
    for num in L:
        if num < Min:
            Min = num
        if num > Max:
            Max = num
    return(Min, Max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')