#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import pyperclip
import time

text_input =  pyperclip.paste()
    
text_input.split('\n\n').pop()

text = text_input

pyperclip.copy(text)
spam = pyperclip.paste()

print("已复制到clipboard")
