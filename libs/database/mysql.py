#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：mysql.py
# 作者：zhangxiaofei
# 日期：2018-04-28
# 功能：Mysql操作类
# -------------------------------------------------------------------------

import pymysql
from ..conf.conf import Conf

class Mysql:


  # -----------------------------------------------------------------------
  # 初始化方法

  def __init__(self, host, username, password, dbname, port=3306):

    # 打开数据库连接
    self.db = pymysql.connect(host=host, port=port, user=username, passwd=password, db=dbname, charset='utf8')



  @classmethod
  def connection(self):

    # 获取配置
    conf = Conf()

    # 得到mysql配置文件
    host, username, password, dbname, port = conf.get_mysql_conf_info()

    # 打开数据库连接
    db = Mysql(host, username, password, dbname, int(port))

    return db




  # -----------------------------------------------------------------------
  # 查询

  def select(self, table, field = '*', where = "", group = "", order = ""):

    # 使用cursor()方法获取操作游标
    cursor = self.cursor()

    # SQL 查询语句
    sql = "SELECT %s FROM %s %s %s %s " % (field, table, where, group, order)

    try:
      # 执行SQL语句
      cursor.execute(sql)

      # 返回查询结果
      return cursor.fetchall()
    except:
      print ("Error: unable to fetch data")

    # 关闭游标
    cursor.close()

    # 关闭数据库连接
    self.close()


  # -----------------------------------------------------------------------
  # 创建表

  def execute(self, sql):

    conn = self.db.cursor()

    result = conn.execute(sql)

    conn.close()

    return result




  def executemany(self, sql, data):

    conn = self.db.cursor()

    conn.executemany(sql, data)

    result = self.db.commit()

    conn.close()

    return result


