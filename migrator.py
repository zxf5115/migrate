#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：migrate.py
# 作者：zhangxiaofei
# 日期：2018-04-27
# 功能：选项类
# -------------------------------------------------------------------------

import os
import re
import datetime

from tools.file.file import File

class Migrator:

  # -----------------------------------------------------------------------
  # 添加选项

  def __init__(self, directory):

    self.directory = directory


  # -----------------------------------------------------------------------
  # 初始化方法，是否存在migrate文件目录，没有自动创建

  def init(self):

    try:

      # 项目目录
      basic_path = os.getcwd()

      # migration 初始文件
      filename = "00000000000001_migration.py"

      # 拼接文件绝对路径
      path = r"%s\%s" % (basic_path, filename)

      # 拼接命令
      command = "d:\work\Python\python %s %s" % (path, '')

      os.system(command)

    except Exception as e:

      print(e)





  # -----------------------------------------------------------------------
  # 创建migrate文件

  def create(self, migration_name):

    file = File()

    migrate = file.read('config/migration.ini', migration_name = migration_name)

    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    file_name = '_'.join([str(timestamp), ('%s.py' % migration_name)])

    path = os.path.join(self.directory, file_name)

    file = open(path, 'w+', encoding = 'utf-8')

    file.write(migrate)

    file.close()



  # -----------------------------------------------------------------------
  # 执行migrate文件

  def execute(self):


    files = self.filename()

    for vo in files:

      print(vo)







  def filename(self):

    try:

      # 项目目录
      basic_path = os.getcwd()

      # 列出文件夹下所有的目录与文件
      temp = os.listdir(basic_path)

      files = list(filter(lambda x: self.ismigration(x), temp))

      return files

    except Exception as e:

      print(e)


  def ismigration(self, filename):

    pattern = r"[0-9]{14}"

    return re.match(pattern, filename)






