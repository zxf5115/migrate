#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：conf.py
# 作者：zhangxiaofei
# 日期：2018-04-21
# 功能：操作配置文件的类
# -------------------------------------------------------------------------

import configparser

class Conf(object):

  def __init__(self):

    # 新建配置对象
    self.conf = configparser.ConfigParser()

    # 读取配置文件
    self.conf.read("config/config.ini", encoding="utf-8")




  # -----------------------------------------------------------------------
  # 获取 获取IP 相关 配置信息

  def get_header_conf_info(self):

    header = self.conf.get('header', 'header')

    return header




  # -----------------------------------------------------------------------
  # 获取 获取IP 相关 配置信息

  def get_crawler_conf_info(self):

    url = self.conf.get('crawler', 'url')
    page = self.conf.getint('crawler', 'page')

    return url,page




  # -----------------------------------------------------------------------
  # 获取 获取IP 相关 配置信息中的 字段信息

  def get_ip_field_conf_info(self):

    field   = self.conf.get('ip', 'field')

    return field




  # -----------------------------------------------------------------------
  # 获取 获取IP 相关 配置信息

  def get_ip_conf_info(self):

    path    = self.conf.get('ip', 'path')
    field   = self.conf.get('ip', 'field')
    message = self.conf.get('ip', 'message')

    proxy_ip_url = self.conf.get('ip', 'proxy_ip_url')
    validation_url = self.conf.get('ip', 'validation_url')

    return path, field, message, proxy_ip_url, validation_url




  # -----------------------------------------------------------------------
  # 获取 User Agent 配置中的 字段信息

  def get_user_agent_field_conf_info(self):

    field   = self.conf.get('user_agent', 'field')

    return field




  # -----------------------------------------------------------------------
  # 获取 User Agent 配置信息

  def get_user_agent_conf_info(self):

    path    = self.conf.get('user_agent', 'path')
    field   = self.conf.get('user_agent', 'field')
    message = self.conf.get('user_agent', 'message')

    return path, field, message



  # -----------------------------------------------------------------------
  # 获取 Log 配置信息

  def get_log_conf_info(self):

    level = self.conf.get('log', 'level')

    return level



  # -----------------------------------------------------------------------
  # 获取 Redis 配置信息

  def get_redis_conf_info(self):

    host = self.conf.get("redis", "host")
    port = self.conf.get("redis", "port")

    return host, port




  # -----------------------------------------------------------------------
  # 获取 Mysql 配置信息

  def get_mysql_conf_info(self):

    host     = self.conf.get("mysql", "host")
    username = self.conf.get("mysql", "username")
    password = self.conf.get("mysql", "password")
    dbname   = self.conf.get("mysql", "dbname")
    port     = self.conf.get("mysql", "port")

    return host, username, password, dbname, port
