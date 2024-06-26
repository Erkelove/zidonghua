import json
import re
import jsonpath
import jmespath
from utils import exceptions
from requests import Response


def extract_by_object(response: Response, extract_expression: str):
    """
    从response 对象属性取值 [status_code, url, ok, headers, cookies, text, json, encoding]
    :param response: Response Obj
    :param extract_expression:
    :return:
    """
    if not isinstance(extract_expression, str):
        return extract_expression
    res = {
        "headers": response.headers,
        "cookies": dict(response.cookies)
    }
    if extract_expression in ["status_code", "url", "ok", "encoding"]:
        return getattr(response, extract_expression)
    elif extract_expression.startswith('headers') or extract_expression.startswith('cookies'):
        return extract_by_jmespath(res, extract_expression)
    elif extract_expression.startswith('body') or extract_expression.startswith('content'):
        try:
            response_parse_dict = response.json()
            return extract_by_jmespath({'body': response_parse_dict}, extract_expression)
        except Exception as msg:
            raise exceptions.ExtractExpressionError(f'expression:<{extract_expression}>, error: {msg}')
    elif extract_expression.startswith('$.'):
        try:
            response_parse_dict = response.json()
            return extract_by_jsonpath(response_parse_dict, extract_expression)
        except Exception as msg:
            raise exceptions.ExtractExpressionError(f'expression:<{extract_expression}>, error: {msg}')
    elif '.+?' in extract_expression or '.*?' in extract_expression:
        # 正则匹配
        return extract_by_regex(response.text, extract_expression)
    else:
        # 其它非取值表达式，直接返回
        return extract_expression

def extract_by_jsonpath(extract_obj: dict, extract_expression: str):
    """
    jsonpath提取
    :param extract_obj: response.json()
    :param extract_expression: '$.code'
    :return: NONE or first value and all value
    """
    if not isinstance(extract_expression, str):
        return extract_expression
    extract_value = jsonpath.jsonpath(extract_obj, extract_expression)
    if not extract_value:
        return
    elif len(extract_value) == 1:
        return extract_value[0]
    else:
        return extract_value

def extract_by_jmespath(extract_obj: dict, extract_expression: str):
    """
    jmespath提取
    :param extract_obj: {"body": response.json(), "cookies": dict(response.cookies)}
    :param extract_expression: body.code
    :return: NONE or first value and all value
    """
    if not isinstance(extract_expression, str):
        return extract_expression
    try:
        extract_value = jmespath.search(extract_expression, extract_obj)
        return extract_value
    except Exception as msg:
        raise exceptions.ExtractExpressionError(f'expression:<{extract_expression}>, error: {msg}')

def extract_by_regex(extract_obj: str, extract_expression: str):
    """
    正则表达式提取返回结果
    :param extract_obj: must type str
    :param extract_expression:
    :return:
    """
    if not isinstance(extract_expression, str):
        return extract_expression
    extract_value = re.findall(extract_expression, extract_obj, flags=re.S)  # re.S:允许跨多行匹配
    if not extract_value:
        return ''
    elif len(extract_value) == 1:
        return extract_value[0]
    else:
        return extract_value
