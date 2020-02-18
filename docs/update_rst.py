#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Luo-Songtao
# Email: ryomawithlst@gmail/outlook.com
import os 

modules = ["data_structures", "divide_and_conquer", "dynamic_programming", "greedy_algorithm", "trees", "sort"]

for module in modules:
    os.system("rm -rf source/{module}".format(module=module))
    os.system("sphinx-apidoc -f -E -a -M -o source/rst/{module} ../src/{module}".format(module=module))
