if __name__ == '__main__':
    (A,n) = (
        set(raw_input().split(' ')),
        int(raw_input())
    )
    response = []
    for _ in range(n):
        B = set(raw_input().split(' '))
        response.append((A & B != A) & (A & B == B))

    print(all(response))
    
