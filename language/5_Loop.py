from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    print ("\n".join([str(i**2) for i in range(n) if n in range(1,21)]))
