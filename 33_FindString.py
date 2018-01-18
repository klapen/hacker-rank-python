def count_substring_for(string, sub_string):
    sub_len,str_len = len(sub_string),len(string)
    res = 0
    if str_len > sub_len:
        for i in range(0,str_len-sub_len+1):
            slice_str = string[i:sub_len+i]
            if len(slice_str) < sub_len:
                break
            elif slice_str == sub_string:
                res += 1
    return res

def count_substring(string, sub_string):
    sub_len,str_len = len(sub_string),len(string)
    return sum([1 for i in range(0,str_len-sub_len+1) if string[i:sub_len+i] == sub_string])

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
