import os

import pytest

if __name__ == '__main__':
    pytest.main()
    # pytest.main(['-vs', './program', '--alluredir=./temp'])

    os.system('allure generate ./temp -o ./report --clean')