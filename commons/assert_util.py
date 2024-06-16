def assert_equal(actual, expected):
    if actual != expected:
        raise AssertionError(f"Actual: {actual}, Expected: {expected}")

def assert_not_equal(actual, expected):
    if actual == expected:
        raise AssertionError(f"Actual: {actual}, Expected: {expected}")

def assert_true(condition):
    if not condition:
        raise AssertionError(f"Condition is not True")

def assert_false(condition):
    if condition:
        raise AssertionError(f"Condition is not False")

def assert_contains(container, item):
    if item not in container:
        raise AssertionError(f"Item: {item} is not in container")

def assert_not_contains(container, item):
    if item in container:
        raise AssertionError(f"Item: {item} is in container")
def assert_sort(list):
    a = 1
    for i in range(len(list)):
        if list[1] < list[0]:
            raise AssertionError("当前列表数据排序错误！")