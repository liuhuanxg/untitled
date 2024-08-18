# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 242.valid_anagram.py

eg：
    rat tar
    cat atc
    anagram nagamar

"""


def format(s):
    dct = {}
    for i in s:
        dct[i] = dct.get(i, 0) + 1
    return dct


def valid_anagram1(s, t):
    if len(s) != len(t):
        return False
    dct_s = format(s)
    dct_t = format(t)

    return dct_s == dct_t


def valid_anagram2(s, t):
    return sorted(s) == sorted(t)


if __name__ == '__main__':
    print(valid_anagram1("rat", "tar"))
    print(valid_anagram2("rat", "tar"))
