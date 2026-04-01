from app import add, subtract

def test_add():
    assert add(1, 2) == 3
    print("test_add 通過！")

def test_subtract():
    assert subtract(5, 3) == 2
    print("test_subtract 通過！")

test_add()
test_subtract()
print("所有測試通過！")