#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com

class BTreeNode:
    """B树节点
    
    Attributes:
        leaf: 布尔类型值。为True则表示当前节点是叶节点
        keys_count: 记录当前节点上存储的关键字个数
        depth: 记录当前节点的高度
        keys: 存储当前节点存放的关键字
        child_nodes: 存储当前节点的子节点(指针)
    
    """
    
    def __init__(self):
        self.leaf = True
        self.keys_count = 0    # 节点关键字个数
        self.depth = 0
        self.keys = []    # lenth = keys_count
        self.child_nodes = []    # length = keys_count + 1
        self.parent = None

    def get_key(self, i):
        return self.keys[i]
    
    def get_child_node(self, i):
        return self.child_nodes[i]
    
    def pop_key(self, i):
        return self.keys.pop(i)
    
    def pop_child_node(self, i):
        return self.child_nodes.pop(i)
    
    def insert_key(self, key, i=None):
        if i == None:
            self.keys.append(key)
        else:
            self.keys.insert(i, key)

    def insert_child_node(self, node, i=None):
        if i == None:
            self.child_nodes.append(node)
        else:
            self.child_nodes.insert(i, node)
        node.parent = self

class BTree:
    """B树
    
    B树是为磁盘或其他直接存取的辅助存储设备而设计的一种平衡搜索树。B树类似于红黑树。但B树在降低磁盘I/O操作树方面更好一些。
    
    B树与红黑树的不同之处在于B树的节点可以有很多子节点，可以从数个到数千个。
    
    B树以一种自然方式推广了二叉搜索树：如果B树的一个节点拥有n个关键字，那么该节点就会有n+1个子节点
    
    **B树的性质**：
        1. 每个节点有以下属性：
            - keys_count，存储当前节点中关键字个数
            - keys_count个关键字，并以非降序存放
            - leaf，一个布尔值，当前节点是叶节点则为True，否则为False
        2. 每个内部节点还包含keys_count+1个指向其孩子的指针，但注意叶子节点没有子节点，所以它们不需维护这样的指针
        3. 节点上的关键字对存储在各个子树中的关键字的范围加以分割
        4. 每个叶节点具有相同的深度。即树的高度h
        5. 每个节点所包含的关键字个数有上界和下届。用一个被称为B树的**最小度数(minmum degree)**的固定整数来表示这些界
            - 除了根节点以外的每个节点必须至少有minmum_degree-1个关键字。因此除了根节点以外的每个内部节点至少有minmum_degree个子节点。如果树非空，则根节点至少又一个子节点。
            - 每个节点至多可拥有2minmum_degree-1个关键字。因此，一个内部节点至多有2minmum_degree个子节点。
            - 满节点：拥有2minmum_degree-1个关键字
        最小度数为2的B树是最简单的。同时t的值越大，B树的高度也就越小。
    
    """
    
    def __init__(self):
        self.root: BTreeNode = None
        self.minmum_degree = None
    
    def allocate_node(self) -> BTreeNode:
        """模拟在O(1)的时间内为新节点分配一个磁盘页
        """
        return BTreeNode()

    def disk_read(self, node):
        """模拟数据读取磁盘I/O操作
        """
        pass
    
    def disk_write(self, node):
        """模拟数据写入磁盘I/O操作
        """
        pass

    def search(self, key):
        """搜索具有指定key值的节点对象
        
        Returns:
            (node, i): 含有值为key的节点对象以及该key在该节点的索引位置。如果没有查寻到则返回None
        """
        return self._search(self.root, key)
    
    def _search(self, node: BTreeNode, key):
        """在节点上进行线性搜索查找指定key对象
        
        如果没有则递归到对应的子节点，直到叶子节点也没有，将返回None
        """
        for i in range(node.keys_count):
            if key > node.get_key(i):
                i += 1
            elif key == node.get_key(i):
                return (node, i)
            else:
                break
        if node.leaf is True:
            return None, None
        if i < node.keys_count:
            child_node = node.get_child_node(i)
        else:
            child_node = node.get_child_node(i+1)
        self.disk_read(child_node)    
        return self._search(child_node, key)
    
    def create(self):
        """创建一颗空的B树
        """
        node = self.allocate_node()
        node.leaf = True
        node.keys_count = 0
        self.disk_write(node)
        self.root = node
    
    def split_child(self, node: BTreeNode, i):
        """节点分裂
        
        分裂步骤:
            - 当node节点第i个子节点达到2*minmum_degree-1个关键词时，将要对其进行分裂，将第i个子节点的第i个关键词提到node中
            - 建立一个新节点，将第i个子节点的第(minmum_degree), ...,第(2*minmum_degree-1)的(minmum_degree-1)个关键词放入新节点中
            - 并把新节点作为node的第i+1个子节点
        
        注意: 如果node节点的第i个子节点关键字个数低于最小度数-1，这里将会抛出异常
        
        Args:
            node (BTreeNode): 将要分裂的节点的父节点
            i (int): 表明node节点的第i个子节点将要进行分裂。i=0,1,2,...
        """
        the_child = node.get_child_node(i)
        if the_child.keys_count < self.minmum_degree - 1:
            raise Exception("未达到分裂条件")
        
        i_left_child = the_child
        i_right_child = self.allocate_node()
        i_right_child.leaf = i_left_child.leaf
        i_right_child.keys_count = self.minmum_degree - 1
        i_right_child.parent = node
        
        for _ in range(i_right_child.keys_count):    # 把后半部分的key移到新的节点
            i_right_child.insert_key(i_left_child.pop_key(self.minmum_degree))
            
        if not i_left_child.leaf:
            for _ in range(i_right_child.keys_count+1):    # 把后半部分的子节点指针移到新节点
                i_right_child.insert_child_node(i_left_child.pop_child_node(self.minmum_degree))
        
        node.insert_key(i, i_left_child.pop_key(self.minmum_degree-1))
        node.insert_child_node(i, i_left_child.pop_child_node(self.minmum_degree-1))
        
        node.keys_count += 1
        i_left_child.keys_count = self.minmum_degree - 1
        
        self.disk_write(node)
        self.disk_write(i_left_child)
        self.disk_write(i_right_child)
        
    def insert(self, key):
        """插入关键字
        
        插入新关键字，最终是向叶子节点中进行插入，但是为了保证插入后每一个节点的关键字个数不超过2*minmum_degree-1个，那么需要从根节点开始，递归的向下进行判断。
        
        插入步骤:
            - 首先从根节点开始，先判断根节点是否已经达到2*minmum_degree-1个关键字,如果达到了，则需要先对根节点进行分裂
            - 否则将从根节点开始往下递归判断，在每一层当遇到当前节点已经满足2*minmum_degree-1个关键字的，都要先对该节点进行分裂
            - 最后直到叶节点后，不再递归，并将关键字插入到对应的叶节点上
        """
        node = self.root
        if node.keys_count == 2*self.minmum_degree - 1:
            new_node = self.allocate_node()
            self.root = new_node
            new_node.leaf = False
            new_node.keys_count = 0
            new_node.insert_child_node(node)
            self.split_child(new_node, 0)
            self._insert(new_node, key)
        else:
            self._insert(node, key)
    
    def _insert(self, node: BTreeNode, key):
        """insert函数的辅助函数，完成递归判断与最终插入关键字的操作
        """
        i = node.keys_count
        if node.leaf:
            while i >= 0 and key < node.get_key(i):
                i -= 1
            i += 1
            node.insert_key(i, key)
            node.keys_count += 1
        else:
            while i >= 0 and key < node.get_key(i):
                i -= 1
            i += 1
            the_child = node.get_child_node(i)
            self.disk_read(the_child)
            if the_child.keys_count == 2*self.minmum_degree - 1:
                self.split_child(node, i)
                if key > node.get_key(i):
                    the_child = node.get_child_node(i+1)
            self._insert(the_child, key)
    
    def delete(self, key):
        """删除指定的key
        
        删除具有指定的key后，需要保证每一个非根节点的关键字个数不低于minmum_degree-1个。
        
        删除时一方面不仅要沿树下降一次，同时为了保持B树的性质，有可能需要回溯到父节点进行调整。可以采取两种方案进行回溯：
            - 在每一个node上添加parent指针，然后再通过再parent节点上进行查找来确定在parent上node的指针位置
            - 每次需要回溯时，重新沿树下降一次，降到父节点
        
        删除需要的情况(删除要处理的情况比插入时要复杂)，假设要删除的key就在树中：
            - 确定key所在的节点是内部节点还是叶节点
                - 情况1：如果是叶节点，且叶节点的关键字数多于最小度数-1，那么直接在叶结点删除key
                - 情况2：如果是叶节点，且叶节点的关键字数等于最小度数-1，由于删除后不满足B树性质，因此需要做出调整：
                    - a. 首先找到该叶节点的兄弟前驱或兄弟后继节点，如果他们中任意一个的关键字数多于最小度数-1个，那么从该兄弟中剔除一个出来，上升到父节点，并且从父节点中的下降一个到当前的叶节点，然后就回到了情况1
                    - b. 如果该叶节点的兄弟前驱或兄弟后继节点的关键字数都是最小度数-1，那么此时就会发生节点合并。并且此时需要看父节点的关键字数
                        - a. 如果父节点的关键字数多于最小度数-1个，那么从父节点中下降一个k，然后将k与当前叶节点以及它的其中一个相邻兄弟节点合并，这样又回到情况1(此时新的合并节点关键字个数是2*最小度数-1)
                        - b. 如果父节点的关键字数等于最小度数-1，那么由于父节点此时不能下降一个k出来，因此就需要对父节点进行一次合并，然后才能回到情况2.a.a
                - 情况3：如果是内部节点，且关键字数多于最小度数-1，那么需要看当前key的子"前驱"和子"后继"
                    - a. 如果它们俩中其中一个的关键字数多于最小度数-1个，那么直接从中提取一个上来，替换key所在的位置即可
                    - b. 如果它们俩的关键字数都是最小度数-1个，那么就需要先合并它们俩；然后直接从它们的父节点中删除key，并修改相应的指针
                - 情况4：如果是内部节点，且关键字数等于最小度数-1，同样需要看当前key的子"前驱"和子"后继"
                    - a. 同情况3.a
                    - b. 如果它们俩的关键字数都是最小度数-1个，那么此时就只能对这个内部节点进行合并，然后再回到情况3.b来处理
        
        """
        self._delete(key, self.root, None, None)
        
    def _delete(self, key, node: BTreeNode, pre_node, succeed_node):
        """
        
        Args:
            key:
            node: 
            pre_node: node的前驱节点，且与node具有相同父节点
            succeed_node: node的后继节点，且与node具有相同父节点
        """
        # 功能未全部完成
        def find_index_lt_key(node, key):
            for i in range(node.keys_count):
                if key > node.get_key(i):
                    i += 1
                else:
                    break
            return i
        
        i = find_index_lt_key(node, key)
            
        if node.leaf is True:
            if key != node.get_key(i):
                raise Exception("Delete Error: the key '{}' not found in trees".format(key))
            if node.keys_count > self.minmum_degree - 1:
                node.pop_key(i)
            else:
                if pre_node is not None and pre_node.keys_count > self.minmum_degree - 1:
                    pre_k = pre_node.pop_key(-1)
                    p_i = find_index_lt_key(node.parent, pre_k)
                    p_k = node.parent.pop_key(p_i)
                    node.parent.insert_key(pre_k, p_i)
                    
                    node.pop_key(i)
                    node.insert_key(p_k, 0)
                elif succeed_node is not None and succeed_node.keys_count > self.minmum_degree - 1:
                    succeed_k = succeed_node.pop_key(0)
                    s_i = find_index_lt_key(node.parent, succeed_k)
                    s_k = node.parent.pop_key(s_i - 1)
                    node.parent.insert_key(s_k, s_i)
                    
                    node.pop_key(i)
                    node.insert_key(s_k)
                else:
                    pass
        else:
            pass
        
        the_child, pre_child, succeed_child = None, None, None
        if i == node.keys_count:
            the_child = node.get_child_node(i+1)
            pre_child = node.get_child_node(i)
            succeed_child = None
        elif i == 0:
            the_child = node.get_child_node(i)
            pre_child = None
            succeed_child = node.get_child_node(i+1)
        else:
            the_child = node.get_child_node(i)
            pre_child = node.get_child_node(i-1)
            succeed_child = node.get_child_node(i+1)
    
            
        
    