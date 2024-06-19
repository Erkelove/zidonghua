
import os

import yaml

#写入
def write_yaml(data):
    with open(os.getcwd()+"/extract.yaml", encoding="utf-8", mode='a+')as f:
        yaml.dump(data, stream=f, allow_unicode=True)


#读取1
def read_yaml(key):
    with open(os.getcwd()+"/extract.yaml", encoding="utf-8", mode='r')as f:
        value = yaml.load(f, yaml.FullLoader)
        if not value:
            return None
        else:
            return value[key]

#清空
def clear_yaml():
    with open(os.getcwd()+"/extract.yaml", encoding="utf-8", mode='w')as f:
        f.truncate()


#读取测试用例
def read_yaml_testcase(yamlpath):
    with open(yamlpath, encoding='utf-8', mode='r')as f:
        value = yaml.load(f, yaml.FullLoader)
        return value

