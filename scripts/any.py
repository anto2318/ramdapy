from equals import equals 

def any(fn, val, list):
    idx = 0
    while(idx < len(list)):
        if(fn(val, list[idx])):
            return True
        idx += 1
    return False
        
if __name__ == '__main__':
    print(any(equals, 3, [1, 2, 3, 4]))