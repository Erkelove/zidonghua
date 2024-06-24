import json
import unittest

import jsonpath
import requests
from jsonpath_ng import parse
from commons.requests_until import RequestUtil
from hotloads.debug_talk import get_all_yaml_files
from commons.yaml_util import *
from ddt import ddt, file_data, unpack


@ddt
class TestApi():
    file_path = os.getcwd()
    print(file_path)
    testcase_path = os.path.join(file_path, "testcases/")
    print(testcase_path)
    yaml_file_paths = get_all_yaml_files(testcase_path)
    print(type(yaml_file_paths), yaml_file_paths)
    if not yaml_file_paths:
        print("yaml文件路径未获")
    else:
        file_paths = ['./Login/get_token.yaml', './Teacher/my_list.yaml']
        #print("测试用例路径："+f"{yaml_file_paths}")
        @file_data(file_paths)
        def test_all_api(self, **caseinfo):
            print('--------------')
            print(caseinfo)
        # file_path = os.getcwd()
        # print(file_path)
        # testcase_path = os.path.join(file_path, "testcases/")
        # print(testcase_path)
        # yaml_file_paths = get_all_yaml_files(testcase_path)
        # print('yaml_file_paths:', f"{yaml_file_paths}")
        # for yaml_file_path in yaml_file_paths:
        #     print("用例重新开始执行啦")
        #
        #     if not yaml_file_path:
        #         print("yaml文件路径未获取")
        #     else:
        #         token = read_yaml('token')
        #         print("token:"f"{token}")
        #         print(type(yaml_file_path), yaml_file_path)
        #         yaml_data = read_yaml_testcase(yaml_file_path)
        #         print(yaml_data)
        #         if not token:
        #             print("------------------------------")
        #             token_data = {}
        #             url = yaml_data[0]['request']['url']
        #             print(url)
        #             method = yaml_data[0]['request'].get('method', 'GET')
        #             print(method)
        #             params = yaml_data[0]['request'].get('params', None)
        #             print(params)
        #             data = yaml_data[0]['request'].get('data', None)
        #             print(type(data), data)
        #             # data = json.dumps(data)
        #             # print(type(data), data)
        #             headers = yaml_data[0]['request'].get('headers', None)
        #             print(headers)
        #             res_data = RequestUtil().send_request(method=method, url=url, data=data, headers=headers)
        #             res_data = res_data.json()
        #             print(res_data)
        #             token = jsonpath.jsonpath(res_data, yaml_data[0]['extract']['token'])
        #             print(token)
        #             token_data['token'] = token[0]
        #             write_yaml(token_data)
        #         else:
        #             print("===========================")
        #             yaml_data[0]['request']['headers']['X-Token'] = f"{token}"
        #             url = yaml_data[0]['request']['url']
        #             method = yaml_data[0]['request'].get('method', 'GET')
        #             params = yaml_data[0]['request'].get('params', None)
        #             data = yaml_data[0]['request'].get('data', None)
        #             if not data:
        #                 pass
        #             else:
        #                 data = data.dumps(data)
        #             headers = yaml_data[0]['request'].get('headers', None)
        #             res_data = RequestUtil().send_request(method=method, url=url, params=params, data=data, headers=headers)
        #             print(res_data.json())
