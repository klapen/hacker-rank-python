def split_and_join(line):
    return '-'.join(line.split(" "))
    
if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
