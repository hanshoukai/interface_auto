# /usr/bin/env python
# coding=utf-8
# import sys
# sys.path.append("D:/pycharm workspace/")
from src.Traversal_testcase import run_case
from commons.sendmail import SendMail

test_case = "D:\PythonWork\interface_auto\interface_excel_log_email_report\\testcase\laohuanglitestcase3.xlsx"
save_case = "D:\PythonWork\interface_auto\interface_excel_log_email_report\\report\guo1.xlsx"
run = run_case()
run.runcase(test_case, save_case)

# sendmail = SendMail()
# sendmail.send_mail(title)
