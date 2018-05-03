#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：00000000000001_migration.py
# 作者：zhangxiaofei
# 日期：2018-05-02
# 功能：migration
# -------------------------------------------------------------------------

import time

from tools.migrate.migration import Migration

class Model(Migration):

  # -----------------------------------------------------------------------
  # 初始化方法

  def __init__(self, table_name):

    super().__init__(table_name)

    if self.exists():

      exit()





  def exists(self):

    sql = "select id from migration where version = '%s'" % (__file__)

    return self.select(sql)






  # -----------------------------------------------------------------------
  # 执行创建命令

  def up(self):

    try:

      self.primary('id', 11, '自增编号')

      self.varchar('version', 50, '', '版本号')

      self.integer('create_time', 10, 0, '创建时间')

      self.primary_key('id')

      self.engine()

      self.charset()

      self.comment('用户信息表')

      self.create()

      print('创建成功')

    except Exception as e:

      print(e)

    finally:

      self.add()





  def add(self):

    try:

      timestamp = int(time.time())

      sql = "insert into migration (version, create_time) values (%s,%s)"
      data= [['00000000000001_migration.py', timestamp]]

      self.insert(sql, data)

    except Exception as e:

      print(e)



if __name__ == '__main__':

  model = Model('migration')
  model.up()
