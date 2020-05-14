import random
import os
from datetime import datetime, timedelta
import numpy as np

def f1(l):
    #function for first question
    index = 0
    for i in range(len(l)):
        if l[i] == max(l):
            index = i
    return index

def f2(l):
    #function for second question
    res = 0
    for x in l:
        if x%2 == 0:
            res += x
        else:
            res -= x
    return res

def f3(x1, y1, x2, y2):
    if x2 == x1:
        return None, None
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b

def f4(l):
    l_new = sorted(l)
    if len(l) % 2 == 0:
        return (l_new[len(l) // 2 - 1] + l_new[len(l) // 2]) / 2
    else:
        return (l_new[(len(l) - 1) // 2])

def f5(l):
    m = sum(l) / len(l)
    return m, (sum([(x-m)**2 for x in l]) / (len(l) - 1))**0.5

def f6(s):
    res = ''
    for x in s:
        if x.lower() == x:
            res += x.upper()
        else:
            res += x.lower()
    return res

def f7(s):
    s_new = s.lower()
    s_new = s_new.replace(',','').replace('.','').replace('?','').replace('!','')
    D = {}
    for word in s_new.split():
        if word not in D:
            D[word] = 1
        else:
            D[word] += 1
    return D

def f8(path):
    with open(path) as f:
        res = [line.strip() for line in f]
    return res

def f9(path):
    res = []
    for x in os.listdir(path):
        if os.path.isdir(os.path.join(path, x)):
            res.append(x)
    return sorted(res)

def f10(s1, s2):
    t1 = datetime.strptime(s1, '%H:%M:%S')
    t2 = datetime.strptime(s2, '%H:%M:%S')
    return (t2 - t1).total_seconds()
