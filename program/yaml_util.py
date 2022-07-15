import os

import yaml


def read_yaml(yaml_name):
    with open(os.getcwd()+'/program/'+yaml_name, mode='r', encoding='utf-8') as file:
        datas = yaml.load(stream=file, Loader=yaml.FullLoader)
        return(datas)

# def read_yaml(yaml_name):
#     with open(os.getcwd()+'/'+yaml_name, mode='r', encoding='utf-8') as file:
#         datas = yaml.load(stream=file, Loader=yaml.FullLoader)
#         return(datas)

