#!/bin/python

import sys

def staircase_for(n):
    # Complete this function
    for c in [' '*(n-i)+'#'*(i) for i in range(1,n+1)]:
        print c

def staircase(n):
    for i in range(1,n+1):
        print ('#'*i).rjust(n,' ')

if __name__ == "__main__":
    n = int(raw_input().strip())
    staircase(n)
