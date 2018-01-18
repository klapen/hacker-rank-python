validators = [lambda x: x.isalnum(),lambda x: x.isalpha(), lambda x: x.isdigit(), lambda x: x.islower(), lambda x: x.isupper()]

def check(func,s):
    res = False
    for c in s:
        if func(c):
            res = True
            break
    return res

def validate_any(s):
    for v in validators:
        print any([v(c) for c in s])

def validate(s):
    for v in validators:
        print check(v,s)

if __name__ == '__main__':
    s = raw_input()
    validate(s)
