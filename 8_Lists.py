from __future__ import print_function
if __name__ == '__main__':
    N = int(raw_input())
    cmds = [str(raw_input()).split(' ') for _ in range(N)]
    arr = []
    functions = {
        'insert': lambda args: arr.insert(int(args[0]),int(args[1])),
        'print': lambda args: print(arr),
        'remove': lambda args: arr.remove(int(args[0])),
        'append': lambda args: arr.append(int(args[0])),
        'sort': lambda args: arr.sort(),
        'pop': lambda args: arr.pop(),
        'reverse': lambda args: arr.reverse()
    }
    [functions[cmd[0]](cmd[1:] if len(cmd) > 1 else []) for cmd in cmds]
