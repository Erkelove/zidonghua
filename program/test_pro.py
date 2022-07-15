import pytest
import requests as requests

from program.yaml_util import read_yaml


class Test_P():

    #yaml文件中如果有两条命令就会循环执行两次，每次放回的都是一组字典类型的请求数据
    @pytest.mark.smoke
    @pytest.mark.parametrize('data', read_yaml('yongli.yml'))
    def test01(self, data):
        print(data)
        method = data['request']['method']
        url = data['request']['url']
        datas = data['request']['data']

        res = requests.request(method=method, url=url, params=datas)
        print(res.text)
        assert res.status_code == 200





