#!D:\python\python.exe

import sys
import io
import pymysql
import cgi
import cgitb

cgitb.enable()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

print("Content-type:text/html;charset=utf-8")
print()



