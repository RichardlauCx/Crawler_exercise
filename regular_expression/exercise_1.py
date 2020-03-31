# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLauCx
#  @ file   : Richard.py
#  @ IDE    : PyCharm

import re


def opera_1():
    a = re.search(r'fox','the quick brown fox jumpred')
    print(a)
    print(a.span())


def opera_2():
    pattern = re.compile(r'\d+')
    result = re.match(pattern, '192abc')
    # print(result.group())

    match_iter = re.finditer(pattern, "A1B2C3D4E5F6")

    for match in match_iter:
        print(match)


if __name__ == '__main__':
    # opera_1()
    opera_2()