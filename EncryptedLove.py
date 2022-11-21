# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:09:01 2020

@author: demon
"""

import random
import string
import time

print("\n","\n")
a = input("Input Encryption Key: ")
print("\n","\n")
time.sleep(3)
if a == "Elizabeth":
    for i in range(1,150):
        rand1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(170))
        print(rand1)
        time.sleep(0.1)
    print("\n","\n","\n","\n")
    time.sleep(3)
    print("Output")
    print("\n","\n","\n","\n")

        