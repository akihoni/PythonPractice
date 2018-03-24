'''
Created on 2018年3月23日

@author: akiho
'''
def trim(s):
    if s[:1] == ' ':
        s = trim(s[1:])
    if s[-1:] == ' ':
        s = trim(s[:-1])
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')