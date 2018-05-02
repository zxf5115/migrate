#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# ����00000000000001_migration.py
# ���ߣ�zhangxiaofei
# ���ڣ�2018-05-02
# ���ܣ�migration
# -------------------------------------------------------------------------

import time

from tools.migrate.migration import Migration

class Model(Migration):

  # -----------------------------------------------------------------------
  # ��ʼ������

  def __init__(self, table_name):

    super().__init__(table_name)




  # -----------------------------------------------------------------------
  # ִ�д�������

  def up(self):

    try:

      self.primary('id', 11, '�������')

      self.varchar('version', 50, '', '�汾��')

      self.integer('create_time', 10, 0, '����ʱ��')

      self.primary_key('id')

      self.engine()

      self.charset()

      self.comment('�û���Ϣ��')

      self.create()

      print('�����ɹ�')

      self.add()

    except Exception as e:

      print(e)


  def add(self):

    try:

      timestamp = int(time.time())

      sql = "insert into migration (id,version, create_time) values (%s,%s, %s)"
      data= [['1','00000000000001_migration.py', timestamp]]

      self.insert(sql, data)

    except Exception as e:

      print(e)



if __name__ == '__main__':

  model = Model('migration')
  model.up()

