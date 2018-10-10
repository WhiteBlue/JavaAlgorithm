#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: whiteblue
# Created : 2016/10/5
import time

import sys


def find_substring(a, b):
    tmp = [[0 for x in range(len(b))] for y in range(len(a))]

    arr = ['\\', '-', '/']

    i = 0

    while True:
        sys.stdout.write('\r' + arr[i % 3])
        sys.stdout.flush()
        i += 1
        time.sleep(0.5)

    # 初始化
    for i in range(len(a)):
        if a.find(b[0], 0, i) > 0:
            tmp[i][0] = 1
    for i in range(len(b)):
        if b.find(a[0], 0, i) > 0:
            tmp[0][i] = 1

    for x in range(1, len(a)):
        for y in range(1, len(b)):
            if a[x] == b[y]:
                tmp[x][y] = tmp[x - 1][y - 1] + 1
            else:
                tmp[x][y] = max(tmp[x - 1][y], tmp[x][y - 1])

    return tmp[len(a) - 1][len(b) - 1]


if __name__ == '__main__':
    print find_substring("fbcabec", "cabefab")
