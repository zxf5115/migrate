#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：file.py
# 作者：zhangxiaofei
# 日期：2018-05-02
# 功能：文件操作类
# -------------------------------------------------------------------------



class File(object):


  # -----------------------------------------------------------------------
  # 初始化方法

  def __init__(self):

    #
    self.handle = None




  # -----------------------------------------------------------------------
  # 读内容

  def read(self, path, mode = 'r', migration_name = ''):

    try:

      replace = '[zhangxiaofei]'

      self.handle = open(path, mode, encoding='UTF-8')

      result = self.handle.read()

      result = result.replace(replace, migration_name)

      return result

    except Exception as e:

      print(e)
