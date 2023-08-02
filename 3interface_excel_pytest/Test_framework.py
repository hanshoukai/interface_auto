import requests
import pytest
from xToolkit import xfile

# 1.读取Excel数据转换成列表
testdata = xfile.read("接口测试用例.xls").excel_to_dict(sheet=1)
print(testdata)
"""
[
    {'描述': '用户登录', '用例编号': 'hc_shop_api_001', '接口URL': 'http://shop-xo.hctestedu.com/index.php?s=api/user/login', '请求方式': 'post', 'URL参数': '{"application":"app","application_client_type": "weixin",}', '表单参数': '', 'JSON参数': ' {"accounts":"huace_xm","pwd": 123456,"type":"username"}', '预期状态码': 200, '预期返回内容': '', '备注': '', '提取参数': 'token', '需要参数': ''},
    {'描述': '加入购物车', '用例编号': 'hc_shop_api_002', '接口URL': 'http://shop-xo.hctestedu.com/index.php?s=api/cart/save', '请求方式': 'post', 'URL参数': '{"application":"app","application_client_type": "weixin",}', '表单参数': '', 'JSON参数': '{"goods_id": "2","spec": [{"type": "套餐","value": "套餐二"},{"type": "颜色","value": "银色"},{"type": "容量","value": "64G"}],"stock": 1}', '预期状态码': 200, '预期返回内容': '', '备注': '', '提取参数': '', '需要参数': 'token'}
 ]
"""
print(type(testdata))
# <class 'list'>
for i in testdata:
    print(i["接口URL"])
"""
http://shop-xo.hctestedu.com/index.php?s=api/user/login
http://shop-xo.hctestedu.com/index.php?s=api/cart/save
"""

# 2、定义全局变量存token
token = []
# 3、提取请求公共方法单独封装成函数
def do_it(url,method,params,data):
    res = requests.request(
        url=url,
        method=method,
        params=params,
        data=data
    )
    return res.json()

# 4、采用pytest参数化的机制实现遍历
@pytest.mark.parametrize("case_info", testdata)
def test_send_request(case_info):
    if case_info["提取参数"] == "token":
        res = do_it(url=case_info["接口URL"],method=case_info["请求方式"],params=eval(case_info["URL参数"]),data=eval(case_info["JSON参数"]))
        get_token = res["data"]["token"]
        token.append(get_token)
        print("token:",token)  # token: ['28daa306db4c532db62fa2a167fe7c64']
        print(res)
        assert res["code"] == 0

    elif case_info["需要参数"] == "token":
        params = eval(case_info["URL参数"])
        params.update({'token': '{}'.format(str(token[0]))})
        # print(params)  # {'application':'app','application_client_type':'weixin','token':'7534300d2c887bac7b67e4ab4d4404cc'}
        res = do_it(url=case_info["接口URL"],method=case_info["请求方式"],params=params,data=eval(case_info["JSON参数"]))
        print(res)
        assert res["code"] == 0


if __name__ == '__main__':
    pytest.main(["-vs", "--capture=sys"])
