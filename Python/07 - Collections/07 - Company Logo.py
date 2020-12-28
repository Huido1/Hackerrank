#url: https://www.hackerrank.com/challenges/most-commons/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import collections



if __name__ == '__main__':
    s = input()
    for k in collections.Counter(sorted(s)).most_common(3):
        print(*k)
