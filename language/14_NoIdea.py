if __name__ == '__main__':
    n,m = raw_input().split(' ')
    arr = [int(i) for i in raw_input().split(' ')]
    happy = set([int(i) for i in raw_input().split(' ')])
    unhappy = set([int(i) for i in raw_input().split(' ')])
    print(sum([(i in happy) - (i in unhappy) for i in arr]))
