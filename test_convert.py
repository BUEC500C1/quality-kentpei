from convert import *
def test():
    assert convert_num(1) == 'I'
    assert convert_num(4) == 'IV'
    assert convert_num(10) == 'X'
    assert convert_num(100) == 'C'
    assert convert_num(90) == 'XC'
    assert convert_num(400) == 'CD'
    assert convert_num(1001) == 'MI'
    assert convert_num(2394) == 'MMCCCXCIV'
