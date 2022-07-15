import json
from configparser import ConfigParser

import yaml

from common import logger

class MyConfigParser(ConfigParser):
    def __init__(self,defaults=None):
        ConfigParser.__init__(self, defaults=defaults)
    #父类方法会将读取的数据转换成小写字母
    def optionxform(self, optionstr: str) -> str:
        return optionstr

class ReadData():

    def __init__(self):
        pass

    def ReadYaml(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        logger.info("加载到的文件{}".format(file_path))
        return data
    def ReadJson(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        logger.info("加载到的文件{}".format(file_path))
        return data

    def ReadIni(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            #logger.info("加载 {} 文件......".format(file_path))
            config = MyConfigParser()
            config.read(file_path, encoding='utf-8')
            data = dict(config._sections)
            print("读到数据 ==>>  {} ".format(data))
            return data
