#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: whiteblue
# Created : 16/8/12


def find_recursion(choices, i, ret_val):
    if ret_val <= 0:
        return 1 if ret_val == 0 else 0

    if i == len(choices):
        return 0

    ret = 0
    target = choices[i]
    length = int(ret_val / target)

    for c in range(0, length + 1):
        ret += find_recursion(choices, i + 1, ret_val - target * c)

    return ret


if __name__ == '__main__':
        choices = [1, 2, 3]

    back = find_recursion(choices, 0, 6)

    print(back)
