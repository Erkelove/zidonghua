import os
from commons.yaml_util import *


def get_all_yaml_files(directory):
    yaml_file_paths = []
    # 使用os.walk遍历文件夹及其所有子文件夹
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                # 获取文件的完整路径
                yaml_file_path = os.path.join(root, file)
                yaml_file_paths.append(yaml_file_path)
    print(yaml_file_paths)
    return yaml_file_paths

def extract_value(response_body, jsonpath_expr):
    matches = [match.value for match in jsonpath_expr.find(response_body)]
    if matches:
        return matches[0]
    return None

def get_token():
    token_data = read_yaml()
    token = token_data['extract']['token']
    return token


