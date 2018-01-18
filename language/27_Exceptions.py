if __name__ == '__main__':
    for _ in range(int(raw_input())):
        try:
            data = raw_input().split(' ')
            print(int(data[0])//int(data[1]))
        except Exception as e:
            print "Error Code:",e
