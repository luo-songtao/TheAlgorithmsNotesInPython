#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Author: luo-songtao
双向链表
'''


class Link:
    """链接表元素"""
    
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return " {} ".format(self.key)

    
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None 
    
    def insert(self, link):
        """
        向链表尾部插入新元素：O(1)
        """
        if self.tail != None:
            self.tail.next = link
            link.prev = self.tail
        else:
            self.head = link
        self.tail = link
        
    def delete(self, link):
        """
        删除链表中的link元素: O(1)
        """
        if link.prev != None:
            link.prev.next = link.next
        else:
            self.head = link.next
        
        if link.next != None:
            link.next.prev = link.prev
        else:
            self.tail = link.prev
    
    def search(self, key):
        """
        根据元素的关键字搜索链表元素：O(n)
        """
        link = self.head
        while link != None and link.key != key:
            link = link.next
        return link
    
    def traversal(self, reverse=False):
        """
        遍历链表
        """
        link = self.head if reverse is False else self.tail
        while True:
            yield link
            if reverse is False and link.next != None:
                link = link.next
            elif reverse is True and link.prev != None:
                link = link.prev
            else:
                break


if __name__ == "__main__":
    linked_list = LinkedList()
    
    keys = [5,23,1,26,21,78,12]
    
    for i in keys:
        linked_list.insert(Link(i))
    
    head = linked_list.head
    tail = linked_list.tail
    print("Head: ", linked_list.head)
    print("Tail: ", linked_list.tail)
    print("Traversal Head2tail: ", list(linked_list.traversal()))
    key = keys[3]
    searched_link = linked_list.search(key)
    print("Searched key={}: ".format(key), searched_link)
    linked_list.delete(searched_link)
    print("Deleted key={}".format(key))
    print("Traversal Tail2head: ", list(linked_list.traversal(True)))
    