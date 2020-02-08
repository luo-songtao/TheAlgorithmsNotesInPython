#!/usr/bin/bash

python update_rst.py

make html

rm -rf ../docs
mv build/html ../docs