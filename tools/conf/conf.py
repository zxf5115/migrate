#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：conf.py
# 作者：zhangxiaofei
# 日期：2018-04-21
# 功能：操作配置文件的类
# -------------------------------------------------------------------------

import configparser

class Conf:

  def __init__(self):

    # 新建配置对象
    self.conf = configparser.ConfigParser()

    # 读取配置文件
    self.conf.read("config/config.ini", encoding="utf-8")





  # -----------------------------------------------------------------------
  # 获取 Log 配置信息

  def get_log_conf_info(self):

    level = self.conf.get('log', 'level')

    return level





  # -----------------------------------------------------------------------
  # 获取 Mysql 配置信息

  def get_mysql_conf_info(self):

    host     = self.conf.get("mysql", "host")
    username = self.conf.get("mysql", "username")
    password = self.conf.get("mysql", "password")
    dbname   = self.conf.get("mysql", "dbname")
    port     = self.conf.get("mysql", "port")

    return host, username, password, dbname, port
