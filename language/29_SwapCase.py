def swap_case(s):
    #return reduce(lambda acc,curr: accc+curr,[c.lower() if c.isupper() else c.upper() for c in s])
    return ''.join([c.lower() if c.isupper() else c.upper() for c in s])


if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
