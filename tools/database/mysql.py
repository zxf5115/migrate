#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：mysql.py
# 作者：zhangxiaofei
# 日期：2018-04-28
# 功能：Mysql操作类
# -------------------------------------------------------------------------

import pymysql

class Mysql(object):


  # -----------------------------------------------------------------------
  # 初始化方法

  def __init__(self, host, username, password, dbname, port=3306):

    # 打开数据库连接
    self.db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='python', charset='utf8')




  # -----------------------------------------------------------------------
  # 创建表

  def execute(self, sql):

    try:

      conn = self.db.cursor()

      result = conn.execute(sql)

      conn.close()

      return result

    except Exception as e:

      print(e)



  def executemany(self, sql, data):

    try:

      conn = self.db.cursor()

      conn.executemany(sql, data)

      result = self.db.commit()

      conn.close()

      return result

    except Exception as e:

      print(e)
