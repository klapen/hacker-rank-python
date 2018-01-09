from __future__ import division

def average(array):
    s_arr = set(array)
    return (sum(s_arr)/len(s_arr))

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
