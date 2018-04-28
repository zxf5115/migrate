#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：migration.py
# 作者：zhangxiaofei
# 日期：2018-04-28
# 功能：migrate 基类
# -------------------------------------------------------------------------

from ..conf.conf import Conf
from ..database.mysql import Mysql

class Migration(object):


  def create(self):

    sql = "CREATE TABLE %s(%s);" % (self.table_name, self.data)
    print(sql)
    return self.handle.execute(sql)




  # -----------------------------------------------------------------------
  # 创建 char 类型 字段

  def char(self, field, length, default = '', comment = ''):

    self.data += " `%s` CHAR(%d) DEFAULT '%s' COMMENT '%s' " % (field, length, default, comment)




  # -----------------------------------------------------------------------
  # 创建 varchar 类型 字段

  def varchar(self, field, length, default = '', comment = ''):

    self.data += " `%s` VARCHAR(%d) DEFAULT '%s' COMMENT '%s', " % (field, length, default, comment)




  # -----------------------------------------------------------------------
  # 创建 text 类型 字段

  def text(self, field, length, comment = ''):

    self.data += " `%s` TEXT(%d) DEFAULT '%s' COMMENT '%s', " % (field, length, comment)


  # -----------------------------------------------------------------------
  # 创建 tinyint 类型 字段

  def tinyint(self, field, length, default = '', comment = '', is_null = 'NOT NULL'):

    self.data += " `%s` TINYINT(%d) %s DEFAULT '%s' COMMENT '%s', " % (field, length, is_null, default, comment)




  # -----------------------------------------------------------------------
  # 创建 int 类型 字段

  def integer(self, field, length, default = '', comment = '', is_null = 'NOT NULL'):

    self.data += " `%s` INT(%d) %s DEFAULT '%s' COMMENT '%s', " % (field, length, is_null, default, comment)





  # -----------------------------------------------------------------------
  # 增加主键

  def primary(self, field, length, comment = ''):

    self.data += " `%s` INT(%d) NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '%s', " % (field, length, comment)



  # -----------------------------------------------------------------------
  # 删除字段

  def remove_field(self, field):

    return " ALTER TABLE %s DROP COLUMN %s " % (self.table_name, field)

  # def add_field(self):

  #   return " ALTER TABLE %s ADD %s "

  #   新增一个字段，默认值为0，非空，自动增长，主键：
  #   alter table tabelname add new_field_name field_type default 0 not null   auto_increment ,add primary key (new_field_name);

  #   5、改变字段的类型：alter table tableName modify field_name field_type;
  # 6、重命名字段：alter table tableName change old_field_name new_field_name new_field_type;


  # -----------------------------------------------------------------------
  # 创建存储类型

  def engine(self, engine):

    return "ALTER TABLE %s ENGINE = %s " % (self.table_name, engine)




  def mysql(self):

    # 获取配置
    conf = Conf()

    # 得到mysql配置文件
    host, username, password, dbname, port = conf.get_mysql_conf_info()

    # 实例化 Mysql 对象
    self.mysql = Mysql(host, username, password, dbname, port)

    return self.mysql


  def sqlite(self):

    #TODO: 暂时未开发
    pass

  def __init__(self, table_name):

    self.table_name = table_name
    self.data = ''

    self.handle = self.mysql()













