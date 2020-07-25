from toUpper import toUpper 

def adjust(idx, fn, list):
    if (idx >= len(list) or idx < -len(list)):
        return list
    start = len(list) if idx < 0 else 0
    _idx = start + idx
    _list = list
    _list[_idx] = fn(list[_idx])
    return _list

if __name__ == '__main__':
    print(adjust(1, toUpper, ['a', 'b', 'c', 'd']))