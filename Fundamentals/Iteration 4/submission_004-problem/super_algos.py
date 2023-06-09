# author: nosifan

def find_min(els):
    """Returns the minimum from a list of elements."""
    
    if els and all(isinstance(n, int) for n in els) and isinstance(els, (list, tuple)):
        min = els[0]
        if len(els) == 1: return min
        if els[1] >= min: els.remove(els[1]); return find_min(els)
        elif els[1] <= min: els.remove(min); return find_min(els)
    
    return -1


def sum_all(els):
    """Returns sum of all numbers in a list"""
    
    if els and all(isinstance(n, int) for n in els) and isinstance(els, (list, tuple)):
        if len(els) == 1:
            return els[0]
        else: return els[-1] + sum_all(els[:len(els)-1])
    
    return -1


def find_possible_strings(charset, n):
    """Returns all possible strings of length n that can be formed from the given set"""
    
    possible_strs = []
    if charset and all(isinstance(c, str) for c in charset) and isinstance(charset, (list, tuple)):
        if n == 0:
            return []
        elif n == 1:
            return charset
    
        for i in range(len(charset)):
            prefix = charset[i]
            for j in find_possible_strings(charset, n - 1):
                possible_strs.append(prefix + j)
    
    return possible_strs


if __name__ == '__main__':
    print(find_min([1,2,3,-3]))
    print(sum_all([1,2,3,-3]))
    print(find_possible_strings(['a', 'b'], 3))

