import pytest


@pytest.fixture(scope='class', autouse=True)
def my_class_fixture():
    print('打开日志')
    yield
    print('关闭日志')

@pytest.fixture(scope='function', autouse=True)
def my_function_fixture():
    print('方法前置准备工作')
    yield
    print('方法后置处理工作')