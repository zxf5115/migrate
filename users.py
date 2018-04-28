#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：migrate.py
# 作者：zhangxiaofei
# 日期：2018-04-27
# 功能：选项类
# -------------------------------------------------------------------------

from tools.migrate.migration import Migration

class Model(Migration):

  def __init__(self, table_name):

    super().__init__(table_name)


  def up(self):


    self.primary('id', 11, '自增编号')

    self.varchar('name', 50, '', '姓名')

    d = self.create()

    print(d)

    # self.engine()



if __name__ == '__main__':

  model = Model('table_name')
  model.up()