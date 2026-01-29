import math
import os
import random
import re
import sys

def even_odd(n):
    if (n%2==0 and n>=6 and n<=20) or n%2!=0:
        print("Weird")
    else: print("Not Weird")



if __name__ == '__main__':
    n = int(input().strip())
    even_odd(n)
