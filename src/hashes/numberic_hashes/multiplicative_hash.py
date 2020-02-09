#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
import math

GOLDEN_RATIO = (math.sqrt(5)+1)/2


def multiplicative_hash(key: int, m=2**32, A=GOLDEN_RATIO-1):
    """乘法散列hash算法
    ·· math::
        h(k) = floor(m*(kA mod 1))
    
    Args:    
        key: 某个数值型数字
        m: 通常取2的幂次
        A: 0<A<1, 比较理想值为GOLDEN_RATIO-1
        
    >>> multiplicative_hash(12, m=2**16)
    27289
    >>> multiplicative_hash(123456, m=2**14)
    67
    """
    return math.floor(m*math.fmod(key*A, 1))

numeric_hashes = {
    "multiplicative_hash": multiplicative_hash
}
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
