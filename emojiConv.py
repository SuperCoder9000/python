# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 22:06:22 2024

@author: KIIT0001
"""

message = input(">")
words = message.split(' ')
emojis = {
    ":(" : "😔",
    ":)" :"😀",
    "<3" : "💖",
    "<---3":"🍆",
    ";)":"😜"
    }
out = ""
for word in words:
    out += emojis.get(word, word) + " "
print(out)