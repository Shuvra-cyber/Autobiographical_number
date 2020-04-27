from math import *

from collections import Counter

def test(x):
    x = str(x)
    if len(x) > 10:
           return False
    c = Counter(x)
    for i, v in enumerate(x):
            if int(v) != c.get(str(i), 0):
                    return False
    return True

print(test(2020))

for i in range(6*(10**10),10**11):
    if test(i) == True:
        print(i)
        
