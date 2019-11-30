def sub(a, b):
    return a-b

def test():
    assert sub(5,3) == 2
    assert sub(4,6) == 2
    assert sub(3,[3]) == 2
    assert sub(5,True) == 4
    assert sub('two',3) == 2