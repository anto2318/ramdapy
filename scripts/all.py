from equals import equals 

def all(fn, val, list):
    idx = 0
    while(idx < len(list)):
        if not fn(val, list[idx]):
            return False
        idx += 1
    return True

if __name__ == '__main__':
    print(all(equals, 3, [3, 3, 3, 3]))