def string_eq(a, b):
    return a == b

def test():
    assert string_eq(True,'Test') == False
    assert string_eq('world','nor') == False
    assert string_eq(1,'okay') == False
    assert string_eq("a", "a") == True