#!/usr/bin/env python
# -*- coding: utf-8 -*-


def min_heap(arr, i):
    while i < len(arr):
        l, r = 2 * i + 1, 2 * i + 2
        next = i
        if l < len(arr) and arr[next] > arr[l]:
            next = l
        if r < len(arr) and arr[next] > arr[r]:
            next = r
        if next == i:
            return
        arr[next], arr[i] = arr[i], arr[next]
        i = next


def max_heap(arr, i):
    while i < len(arr):
        l, r = 2 * i + 1, 2 * i + 2
        next = i
        if l < len(arr) and arr[next] < arr[l]:
            next = l
        if r < len(arr) and arr[next] < arr[r]:
            next = r
        if next == i:
            return
        arr[next], arr[i] = arr[i], arr[next]
        i = next


def sort_min(arr):
    for i in range(0, len(arr)):
        min_heap(arr, i)


def sort_max(arr):
    for i in range(len(arr) - 1, -1, -1):
        max_heap(arr, i)
