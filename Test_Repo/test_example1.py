def string_inc(a, b):
    return a in b

def test():
    assert string_inc('world','or') == True
    assert string_inc('world','nor') == False
    assert string_inc('world','or') == False 