#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：migrate.py
# 作者：zhangxiaofei
# 日期：2018-04-27
# 功能：选项类
# -------------------------------------------------------------------------

import os
import datetime
import calendar


class Migrator(object):

  # -----------------------------------------------------------------------
  # 添加选项

  def __init__(self, directory):

    self.directory = directory


  # -----------------------------------------------------------------------
  # 初始化方法，是否存在migrate文件目录，没有自动创建

  def init(self):

    if os.path.exists(self.directory):

      result = '"%s" already exists' % self.directory

      print(result)

    else:

      os.makedirs(self.directory)




  # -----------------------------------------------------------------------
  # 创建migrate文件

  def create(self, migration_name):

    migrate = """
    import migrate

    class CreateUsers(tools.migrate.Migration):
      def up():
        self.create_table('users')
        self.string('full_name')
        self.string('email')
      def down():
        self.drop_table('users')

    """


    timestamp = calendar.timegm(datetime.datetime.utcnow().utctimetuple())

    file_name = '_'.join([str(timestamp), ('%s.py' % migration_name)])

    path = os.path.join(self.directory, file_name)

    file = open(path, 'w+')

    file.write(migrate)

    file.close()



  # -----------------------------------------------------------------------
  # 执行migrate文件

  def execute(self):



















