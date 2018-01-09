from operator import itemgetter
if __name__ == '__main__':
    arr = []
    for _ in range(int(raw_input())):
        arr.append([raw_input(),float(raw_input())])

    second_highest = sorted(list(set([score for name,score in arr])))[1]
    print('\n'.join([name for name,score in sorted(arr, key=itemgetter(1,0)) if score == second_highest]))
