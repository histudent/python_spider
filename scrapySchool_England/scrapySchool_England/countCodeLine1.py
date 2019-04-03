# -*- coding:utf-8 -*-
"""
# @PROJECT: Study
# @Author: admin
# @Date:   2018-08-30 14:41:12
# @Last Modified by:   admin
# @Last Modified time: 2018-08-30 14:41:12
"""

import os

print(os.getcwd())

# 获取需要统计代码量的.py文件
def count_line(path, total_count):
    list_dir = os.listdir(path)
    print(list_dir)

    # total_list = []
    for l in list_dir:
        # print(os.path.splitext(l))
        # print("===========================")
        # print(l)
        # print(os.path.isdir(l))
        if os.path.isdir(l) is True:
            # print(os.path.join(path, l))
            count_line(os.path.join(path, l), total_count)

        if l.endswith('.py'):
            # print("***")
            pypath = os.path.join(path, l)
            # total_list.append(pypath)
            total_count += count_py_line(pypath)
            print(total_count)
    # return total_count

def count_py_line(pypath):
    count = 0
    # print(open(pypath, encoding='utf-8').readline())
    for file_line in open(pypath, encoding='utf-8').readlines():
        # print(file_line)
        if file_line != '' and file_line != '\n' and file_line.startswith('#') is not True:
            count += 1
    print(pypath + "----", count)
    return count

if __name__ == '__main__':
    path = os.getcwd()
    total_count = 0
    total = count_line(path, total_count)
    # print(total)



















