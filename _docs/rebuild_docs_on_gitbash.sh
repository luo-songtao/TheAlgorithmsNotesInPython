#!/usr/bin/bash

python update_rst.py

./make.bat html

rm -rf ../docs
mv build ../docs