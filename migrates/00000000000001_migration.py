#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：00000000000001_migration.py
# 作者：zhangxiaofei
# 日期：2018-05-02
# 功能：migration
# -------------------------------------------------------------------------

from .tools.migrate.migration import Migration

class Model(Migration):

  # -----------------------------------------------------------------------
  # 初始化方法

  def __init__(self, table_name):

    super().__init__(table_name)




  # -----------------------------------------------------------------------
  # 执行创建命令

  def up(self):


    self.primary('id', 11, '自增编号')

    self.varchar('version', 50, '', '表名')

    self.integer('create_time', 10, '创建时间')

    self.create()



if __name__ == '__main__':

  model = Model('migration')
  model.up()
