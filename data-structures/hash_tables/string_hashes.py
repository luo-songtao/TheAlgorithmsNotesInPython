#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Author: luo-songtao
"""

def elf_hash(string: str):
    """
    >>> elf_hash("中文")
    346199
    >>> elf_hash("abcdefg")
    126462887
    """
    hash = 0
    for i in string:
        hash = (hash << 4) + ord(i)
        temp = hash & 0xf0000000
        if temp != 0:
            hash ^= (temp>>24)
            hash &= ~temp
    return hash & 0x7ffffff

string_hashes = {
    "elf": elf_hash
}

if __name__ == "__main__":
    import doctest
    doctest.testmod()