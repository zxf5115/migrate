  # -----------------------------------------------------------------------
  # 创建migrate文件
from database.mysql import Mysql


def run():

  mysql = Mysql('127.0.0.1', 'root', 'root', 'python')

  table_name = 'users'

  sql = """

     tutorial_id INT NOT NULL AUTO_INCREMENT,
     tutorial_title VARCHAR(100) NOT NULL,
     tutorial_author VARCHAR(40) NOT NULL,
     submission_date DATE,
     PRIMARY KEY ( tutorial_id )

  """
  print(1)
  mysql.table(table_name, sql)



if __name__ == '__main__':

  run()
