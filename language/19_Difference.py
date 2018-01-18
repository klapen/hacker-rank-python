if __name__ == '__main__':
    eng_num = raw_input()
    eng_arr = set(map(int,raw_input().split(' ')))
    fre_num = raw_input()
    fre_arr = set(map(int,raw_input().split(' ')))
    print(len(eng_arr - fre_arr))
