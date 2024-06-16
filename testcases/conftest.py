import pytest

from commons.yaml_util import clear_yaml


@pytest.fixture(scope='function', autouse=True)
def getToken():
    print("用例执行前运行---------------")
    clear_yaml()
    yield
    print("用例执行后运行---------------")