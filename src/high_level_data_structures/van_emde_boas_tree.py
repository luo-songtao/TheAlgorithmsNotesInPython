#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
import math


class VanEmdeBoasNode:
    """van Emde Boas节点(vEB)
    
    Attributes:
        u (int): 全域大小, 大小为 :math:`2^k`,k=0,1,2,...
        min (int): vEB中的最小元素
        max (int): vEB中的最大元素
        summary (VanEmdeBoasNode): 记录cluster信息的vEB指针
        cluster (list[VanEmdeBoasNode]): vEB树的簇数组，数组每个对象指向一个子vEB对象
    """
    
    def __init__(self, u):
        self.u = u
        self.min = None
        self.max = None
        self.summary = self._create_summary()
        self.cluster = self._create_cluster()
    
    def _create_summary(self):
        """自动递归创建summary
        """
        if self.u > 2:
            return VanEmdeBoasNode(self.up_square_root(self.u))
        else:
            return None
    
    def _create_cluster(self):
        """自动创建cluster数组
        """
        return []
    
    @staticmethod
    def up_square_root(u):
        """计算下平方根 :math:`\sqrt[\downarrow]{u}`
        
        :math:`\sqrt[\downarrow]{16} = 4`
        :math:`\sqrt[\downarrow]{8} = 2`
        
        >>> VanEmdeBoasTree.up_square_root(16)
        4.0
        >>> VanEmdeBoasTree.up_square_root(8)
        2.0
        """
        k = math.log2(u)
        if math.fmod(k, 2) == 0:
            return k
        return k+1
    
    @staticmethod
    def down_square_root(u):
        """计算下平方根 :math:`\sqrt[\downarrow]{u}`
        
        :math:`\sqrt[\downarrow]{16} = 4`
        :math:`\sqrt[\downarrow]{8} = 2`
        
        >>> VanEmdeBoasTree.down_square_root(16)
        4.0
        >>> VanEmdeBoasTree.down_square_root(8)
        2.0
        """
        k = math.log2(u)
        if math.fmod(k, 2) == 0:
            return k
        return k-1
    
    def high(cls, x):
        """计算vEB(u)的高位：实际上表示x在vEB(u)树中的簇号
        
        .. math:: high(x) = \lfloor x/\sqrt[\downarrow]{u} \\rfloor
        
        Example:
            >>> VanEmdeBoasTree.high(7, 16)    # 7在vEB(16)的中的簇号是1
            1
            >>> VanEmdeBoasTree.high(7, 8)    # 7在vEB(8)的中的簇号是3
            3
        """
        return math.floor(x/cls.down_square_root(self.u))

    def low(cls, x):
        """计算vEB(u)的低位：实际上表示x在vEB(u)树中对应簇中的索引位置
        
        .. math:: low(x) = x \mod \sqrt[\downarrow]{u}
        
        Example:
            >>> VanEmdeBoasTree.low(7, 16)    # 7在vEB(16)的中1号簇中，其索引是3
            3
            >>> VanEmdeBoasTree.low(7, 8)    # 7在vEB(8)的中的3号簇中，其索引是1
            1
        """
        return int(math.fmod(x, cls.down_square_root(self.u)))
    
    def index(self, x, y):
        """计算元素在vEB中的索引
        
        .. math:: index(x,y) = x * \sqrt[\downarrow]{u} + y
        
        Args:
            x : 表示簇号
            y : 表示在簇中的索引
        """
        return x*self.down_square_root(self.u) + y


class VanEmdeBoasTree:
    """van Emde Boas 树
    
    van Emde Boas 树支持优先队列操作以及一些其他操作，每个操作最坏情况运行时间位 :math:`O(\\lg \\lg n)`。
    
    但这种数据结构限制关键字必须为0~n-1的整数且无重复
    
    """
    
    def __init__(self, u):
        """
        """
        self.u = u
        
    def minimum(self, v: VanEmdeBoasNode):
        """v中的最小元素
        """
        return v.min
    
    def maximum(self, v: VanEmdeBoasNode):
        """v中的最大元素
        """
        return v.max

    def member(self, v: VanEmdeBoasNode, x):
        """判断x是否是属于v的元素
        """
        if x == v.min or x == v.max:
            return True
        elif v.u == 2:
            return False
        else:
            return self.member(v.cluster[v.high(x)], v.low(x))
    
    def successor(self, v: VanEmdeBoasNode, x):
        """在v中寻找大于x的最小元素
        """
        if v.u == 2:
            if x == 0 and v.max == 1:
                return 1
            else:
                return None
        elif v.min != None and x < v.min:
            return v.min
        else:
            max_low = self.maximum(v.cluster[v.high(x)])
            if max_low != None and v.low(x) < max_low:
                offset = self.successor(v.cluster[v.high(x)], v.low(x))
                return v.index(v.high(x), offset)
            else:
                succ_cluster = self.successor(v.summary, v.high(x))
                if succ_cluster == None:
                    return None
                else:
                    offset = self.minimum(v.cluster[succ_cluster])
                    return v.index(succ_cluster, offset)
                
        def predecessor(self, v: VanEmdeBoasNode, x):
            """在v中寻找小于x的最大元素
            """
            if v.u == 2:
                if x == 1 and v.min == 0:
                    return 0
                else:
                    return None
            elif v.max != None and x > v.max:
                return v.max
            else:
                min_low = self.minimum(v.cluster[v.high(x)])
                if min_low != None and v.low(x) > min_low:
                    offset = self.predecessor(v.cluster[v.high(x)], v.low(x))
                    return v.index(v.high(x), offset)
                else:
                    pre_cluster = self.predecessor(v.summary, high(x))
                    if pre_cluster == None:
                        if v.min != None and x > v.min:
                            return v.min
                        else:
                            return None
                    else:
                        offset = self.maximum(v.cluster[v.high(pre_cluster)])
                        return v.index(pre_cluster, offset)
        
        def empty_insert(self, v: VanEmdeBoasNode, x):
            """空树插入
            
            如果v是空树，那么第一次插入，min和max都是相同的值。
            (同时也意味着如果min为None，则当前的v树必定为空)
            """
            v.min = x
            v.max = x
        
        def insert(self, v: VanEmdeBoasNode, x):
            """插入新元素
            """
            if v.min == None:
                self.empty_insert(v, x)
            else:
                if x < v.min:    # 替换min，同时交换x后，在下一步进行处理
                    x, v.min = v.min, x
                if v.u > 2:    # 如果不是基础结构，那么需要考虑向summary插入
                    if self.minimum(v.cluster[v.high(x)]) == None:    # 只有当对应cluster没有元素时才需要在插入时同时对summary也插入
                        self.insert(v.summary, v.high(x))
                        self.insert(v.cluster[v.high(x), v.low(x)])
                    else:
                        self.insert(v.cluster[v.high(x), v.low(x)])
                if x > v.max:
                    v.max = x
                
        def delete(self, v: VanEmdeBoasNode, x):
            """删除元素
            """
            
            if v.min == v.max:    # 只有一个元素的情况
                v.min = None
                v.max = None
            elif v.u == 2:
                if x == 0:
                    v.min = 1
                else:
                    v.min = 0
                v.max = v.min
            else:
                if x == v.min:
                    first_cluster = self.minimum(v.summary)    # 找到
                    x = index(first_cluster, self.minimum(v.cluster[first_cluster]))    # 计算
                    v.min = x
                self.delete(v.cluster[v.high(x)], v.low(x))
                
                if self.minimum(v.cluster[v.high(x)]) == None:
                    self.delete(v.summary, v.high(x))
                    if x == v.max:
                        summary_max = self.maximum(v.summary)
                        if summary_max == None:
                            v.max = v.min
                        else:
                            v.max = index(summary_max, self.maximum(v.cluster[summary_max]))
                elif x == v.max:
                    v.max = index(v.high(x), self.maximum(v.cluster[v.high(x)]))
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    