#!/bin/python3

import math
import os
import random
import re
import sys

def balancedSum(arr):
    for i in range(len(arr)):
        # print(i)
        left_num_list = []
        right_num_list = []
        for j in range(i):
            left_num_list.append(arr[j])
        for k in range(len(arr)-i-1):
            right_num_list.append(arr[len(arr)-k-1])
        # print(left_num_list)
        # print(right_num_list)
        if sum(left_num_list) == sum(right_num_list):
            return i

if __name__ == '__main__':
    arr = [1, 2, 3, 4,6]
    result = balancedSum(arr)
    print(result)
