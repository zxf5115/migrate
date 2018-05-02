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

from ..file.file import File

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

    self.migration()





  # -----------------------------------------------------------------------
  # 创建migrate文件

  def create(self, migration_name):

    file = File()

    migrate = file.read('config/migration.ini', migration_name = migration_name)

    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    file_name = '_'.join([str(timestamp), ('%s.py' % migration_name)])

    path = os.path.join(self.directory, file_name)

    file = open(path, 'w+')

    file.write(migrate)

    file.close()



  # -----------------------------------------------------------------------
  # 执行migrate文件

  def execute(self):


    pass






  def migration(self):

    path = r"E:\WorkSpace\Python\migrate\00000000000001_migration.py"

    os.system("d:\work\Python\python %s" % (path))




  def filename(self):

    rootdir = 'E:\WorkSpace\Python\migrate\migrates'

    # 列出文件夹下所有的目录与文件
    files = os.listdir(rootdir)

    print(len(files))






