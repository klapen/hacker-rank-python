if __name__ == '__main__':
    n = int(raw_input())
    countries = set([])
    [countries.add(raw_input().lower()) for _ in range(n)]
    print(len(countries))
    
