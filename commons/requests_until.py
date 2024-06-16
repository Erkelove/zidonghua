import json

import requests
from commons.yaml_util import *

#统一请求封装
class RequestUtil:

    session = requests.Session()

    def send_request(self, method, url, data=None, **kwargs):
        method = str(method).upper()  # 转化请求方式为大写
        rep = None
        if method == 'GET':
            rep = self.session.request(method=method, url=url, **kwargs)
        else:
            #data = json.dumps(data)  # 不管他传输过来的是什么格式都转化为字符串进行传参
            rep = self.session.request(method=method, url=url, data=data, **kwargs)  # json和data都可以传参，使用data全部包括
        return rep


    # def send_request(self, **kwargs):
    #     #print(**kwargs)
    #     res = self.sess.request(**kwargs)
    #     print(res.text)
    #     return res

    # def send_all_request(self, url, method='GET', params=None, data=None, headers=None):
    #     """
    #     发送接口请求的函数
    #     :param url: 请求的URL
    #     :param method: 请求方法，默认为GET
    #     :param params: URL参数
    #     :param data: 请求体数据
    #     :param headers: 请求头
    #     :return: 响应对象
    #     """
    #     method = method.upper()
    #     print(url, method, data, params, headers)
    #     # test_cases = read_yaml_testcase()
    #     # test_case['request']['headers']['x-authorization-cx'] = f"{auth}"
    #     # url = test_case['request']['url']
    #     # method = test_case['request'].get('method', 'GET')
    #     # params = test_case['request'].get('params', None)
    #     # data = test_case['request'].get('data', None)
    #     # data = json.dumps(data)
    #     # headers = test_case['request'].get('headers', None)
    #
    #     if method == 'GET':
    #         response = self.send_request(url=url, method='GET', params=params, headers=headers)
    #     elif method == 'POST':
    #         response = requests.post(url=url, data=data, headers=headers)
    #     elif method == 'PUT':
    #         response = self.send_request(url=url, method='PUT', data=data, headers=headers)
    #     elif method == 'DELETE':
    #         response = self.send_request(url=url, method='DELETE', params=params, headers=headers)
    #     else:
    #         raise ValueError("Unsupported HTTP method")
    #
    #     return response


    # def send_request_from_yaml(filename, auth):
    #     """
    #     从YAML文件中读取测试用例并发送接口请求
    #     :param file_path: YAML文件路径
    #     """
    #     file_path = getPath.get_yaml_path(filename)
    #     test_cases = read_yaml_testcase()
    #     for test_case in test_cases:
    #         test_case['request']['headers']['x-authorization-cx'] = f"{auth}"
    #         url = test_case['request']['url']
    #         method = test_case['request'].get('method', 'GET')
    #         params = test_case['request'].get('params', None)
    #         data = test_case['request'].get('data', None)
    #         data = json.dumps(data)
    #         headers = test_case['request'].get('headers', None)
    #         response = send_request(url, method, params, data, headers)
    #         response = response.json()
    #         log.info(response)



