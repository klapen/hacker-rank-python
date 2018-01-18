if __name__ == '__main__':
    arr_len = raw_input()
    arr = set(map(int,raw_input().split(' ')))
    N = int(raw_input())
    cmds = [str(raw_input()).split(' ') for _ in range(N)]
    functions = {
        'remove': lambda args: arr.remove(int(args[0])),
        'pop': lambda args: arr.pop(),
        'discard': lambda args: arr.discard(int(args[0]))
    }
    [functions[cmd[0]](cmd[1:] if len(cmd) > 1 else []) for cmd in cmds]
    print(sum(arr))
