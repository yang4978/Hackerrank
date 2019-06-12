#https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the organizingContainers function below.
def organizingContainers(container):
    container_capacity=[];
    ball_quantity=[];
    for i in range(len(container)):
        container_capacity.append(sum(container[i]))
        ball_quantity.append(sum([arr[i] for arr in container]))
    return 'Possible' if sorted(ball_quantity)==sorted(container_capacity) else 'Impossible'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
