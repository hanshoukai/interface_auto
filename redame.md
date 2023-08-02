### 四种接口自动化脚本编写思路

#### 第一种

> 1interface_ddt_unittest_yaml
>
> > api_keys：封装了请求方式，同时也做了URL和headers的判断处理，测试环境的取值
> >
> > conf：定义了配置文件ini，conf.py是对配置文件的读和写操作
> >
> > ```ini
> > [servers]
> > test = http://test.test.com/
> > pre = http://pre.test.com/
> > online = http://onlien.test.com/
> > 
> > [token]
> > token = 67bcbd0be8adaa5d608de656a11c1574
> > ```
> >
> > test_cases：采用unittest单元测试框架加ddt数据驱动方式调用封装的请求，关联参数的处理
> >
> > - 采用全局变量的形式存储token值
> > - 采用写入配置文件的形式存储token值
> >
> > test_data：采用yaml文件的形式编写测试用例
> >
> > ```yaml
> > -
> >   path: ?s=api/user/login
> >   data:
> >     accounts: test123
> >     pwd: 123456
> >     type: username
> > ```

#### 第二种

> 2interface_excel_log_email_report
>
> > commons：封装了日志类和发送邮件的类
> >
> > log：存放执行日志的地方
> >
> > report：报告采用的是Excel的形式存储
> >
> > src：核心代码部分
> >
> > > interfaceclass.py 封装接口请求及检查点
> > >
> > > Requestclass.py 定义请求方式及发送请求
> > >
> > > Traversal_testcase.py 读取Excel调用发送请求并将响应写入Excel生成报告，同时如果有关联参数做关联处理
> >
> > testcase：采用Excel的形式编写测试用例
> >
> > > laohuanglitestcase1为给的case，且只有一条数据
> > > laohuanglitestcase2为老皇历的三种请求方式post（form）post（json）和get
> > > laohuanglitestcase3其中第二条请求的结果为下一条请求的参数
> >
> > run.py：程序的主入口

#### 第三种

> 3interface_excel_pytest
>
> >Test_framework.py 
> >
> >> 1、读取Excel文件内容
> >>
> >> 2、定义全局变量存放关联的token
> >>
> >> 3、封装请求方法
> >>
> >> 4、采用pytest参数化的方式遍历已经读取的Excel内容，调用请求并做断言
>
> Excel测试用例

#### 第四种

> 4interface_excel
>
> > api_online_request.py
> >
> > > 1、读取Excel文件内容
> > >
> > > 2、接口请求并获取耗时时间
> > >
> > > 3、调用画图函数将图片及请求接口响应 写入Excel报告
> >
> > bingtu.py：绘制饼图函数