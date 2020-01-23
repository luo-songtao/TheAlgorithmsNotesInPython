#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Author: luo-songtao
"""
import math

GOLDEN_RATIO = (math.sqrt(5)+1)/2


def multiplicative_hashing(key: int, m=2**32, A=GOLDEN_RATIO-1):
    """
    乘法散列: h(k) = floor(m*(kA mod 1))
    key: 某个数值型数字
    m: 通常取2的幂次
    A: 0<A<1, 比较理想值为GOLDEN_RATIO-1
    >>> multiplicative_hashing(12, m=2**16)
    27289
    >>> multiplicative_hashing(123456, m=2**14)
    67
    """
    return math.floor(m*math.fmod(key*A, 1))

numeric_hashes = {
    "multiplicative_hashing": multiplicative_hashing
}
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
