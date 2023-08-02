# /usr/bin/env python
# -*- coding: utf-8 -*-
import requests, openpyxl, re
from bingtu import pie_chart


def read_excel():
    path_file = 'D:/PythonWork/interface_auto/4interface_excel/api_online_requestdata.xlsx'
    wp = openpyxl.load_workbook(path_file)
    # sheet = wp.get_sheet_by_name("test")
    sheet = wp.get_sheet_by_name(wp.get_sheet_names()[1])
    for i in range(2, sheet.max_row + 1):
        if sheet.cell(row=i, column=4).value.replace("\n", "").replace("\r", "") == "no":
            continue
        url = sheet.cell(row=i, column=2).value.replace("\n", "").replace("\r", "")
        data = sheet.cell(row=i, column=3).value.replace("\n", "").replace("\r", "")
        # 取出检查点
        check = sheet.cell(row=i, column=6).value.replace("\n", "").replace("\r", "")
        request_url = url + data
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch"}
        res = requests.get(url=request_url, headers=headers)
        # 将接口响应时间写入Excel第五列中
        sheet.cell(row=i, column=5).value = str(res.elapsed.total_seconds())
        # 检查点校验
        if re.search(check, str(res.text)):
            sheet.cell(row=i, column=7).value = "成功"
            sheet.cell(row=i, column=8).value = str(res.text)
        else:
            sheet.cell(row=i, column=7).value = "失败"
            sheet.cell(row=i, column=8).value = str(res.text)

    pie_chart(wp)
    wp.save("D:/PythonWork/interface_auto/4interface_excel/api_online_requestdata_report.xlsx")


# read_excel()
if __name__ == '__main__':
    read_excel()
