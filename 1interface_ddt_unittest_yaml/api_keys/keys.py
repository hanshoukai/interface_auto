import requests
from conf import conf


class ApiKeys:
    # get
    def do_get(self, path=None, headers=None, params=None, **kwargs):
        url = self.set_url(path)
        headers = self.set_headers(headers)
        return requests.get(url=url, headers=headers, params=params, **kwargs)

    # post
    def do_post(self, path=None, headers=None, data=None, json=1, **kwargs):
        url = self.set_url(path)
        headers = self.set_headers(headers)
        if json:
            respones = requests.post(url=url, headers=headers, json=data, **kwargs)
        else:
            respones = requests.post(url=url, headers=headers, data=data, **kwargs)
        return respones

    def set_url(self, path=None):
        # 设置测试环境入口
        base_url = conf.read('servers', 'test')
        if path:
            full_url = base_url + path
        return full_url

    def set_headers(self, headers=None):
        # 定义通用的基础头信息
        base_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
        }
        if headers:
            base_headers.update(headers)
        # 如果有新的token,需要存放在header中再发送请求
        # if conf.read('token', 'token'):
        #     base_headers['token'] = conf.read('token', 'token')
        return base_headers

