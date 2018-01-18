#if __name__ == '__main__':
#    (_, rooms) = (
#        raw_input(),
#        raw_input().split(' ')
#    )
        
#    response = [room for room in rooms if len(filter(lambda x: room == x,rooms)) == 1]
#    print(response[0])

if __name__ == '__main__':
    (K, rooms) = (
        int(raw_input()),
        map(int,raw_input().split(' '))
    )
    unique = set(rooms)
    print(((sum(unique)*K)-(sum(rooms)))//(K-1))
