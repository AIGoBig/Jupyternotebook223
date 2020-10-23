#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import pyperclip
import time

text_input =  pyperclip.paste()
text_input_fin = text_input.replace('示例', '``` python\n'+'示例',1)

local_time = time.strftime('%Y-%m-%d %H:%M ', time.localtime())
text = '### ' + local_time + text_input_fin + '\n```'

pyperclip.copy(text)
spam = pyperclip.paste()

print(spam, "\n\n已复制到clipboard")
