if __name__ == '__main__':
    a_num = raw_input()
    a_arr = set(map(int,raw_input().split(' ')))
    b_num = raw_input()
    b_arr = set(map(int,raw_input().split(' ')))
    print('\n'.join(str(num) for num in sorted(a_arr ^ b_arr)))
