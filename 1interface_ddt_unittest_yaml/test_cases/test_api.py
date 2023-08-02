import unittest
from api_keys.keys import ApiKeys
from ddt import ddt, file_data
from conf.conf import write
from conf.conf import read


@ddt
class TestApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.api = ApiKeys()
        # token采用全局变量的形式保存
        # cls.token = None

    @file_data('../test_data/login.yaml')
    def test_01_login(self, **kwargs):
        # api = ApiKeys()
        # 以下两种都可以实现
        # res = self.api.do_post(path=kwargs['path'], data=kwargs['data'])
        res = self.api.do_post(**kwargs, json=0)

        print(res.json())
        # 1 token采用全局变量的形式保存
        # TestApi.token = res.json()['data']['token']
        # 2 写入文件实现关联数据
        write("token", "token",  res.json()['data']['token'])

    @file_data('../test_data/jiagouwuche.yaml')
    def test_02_jiagouwuche(self, **kwargs):
        # api = ApiKeys()
        # 全局变量的形式保存token打印出来
        # print("打印token：", self.token)
        # 全局变量的形式拼接URL
        # kwargs['path'] = kwargs['path'] + "&token=" + self.token
        # 读取配置文件形式拼接URL
        kwargs['path'] = kwargs['path'] + "&token=" + read('token', 'token')
        print("kwargs内容是：", kwargs)
        res = self.api.do_post(**kwargs)
        print(res.text)


if __name__ == '__main__':
    unittest.main()



