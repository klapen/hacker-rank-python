if __name__ == '__main__':
    num = int(raw_input())
    response = "Weird"
    if num % 2 == 0:
         if num > 20 or num in range(2,5):
             response = "Not Weird" 
    print (response)
