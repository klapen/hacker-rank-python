if __name__ == '__main__':
    (_, A, lines) = (
        raw_input(),
        set(raw_input().split(' ')),
        int(raw_input())
    )
        
    [getattr(A,raw_input().split(' ')[0])(raw_input().split(' ')) for _ in range(lines)]
    print(sum(map(int,A)))
