#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# -------------------------------------------------------------------------
# 程序：migrate.py
# 作者：zhangxiaofei
# 日期：2018-04-27
# 功能：选项类
# -------------------------------------------------------------------------

from libs.migrate.migrator import Migrator
from libs.migrate.options import Options

migrate = Migrator('migrates')

# python migrate.py --init
# python migrate.py --create-migration create_users
options = Options()
options.add('-init', migrate.init)
options.add('-migrate', 'migrate')
options.add('-rollback', 'rollback')
options.add('-create', migrate.create)
options.add('-execute', migrate.execute)
options.add('-remove', 'remove_migration')
options.add('-load-schema', 'load_schema')
options.add('-dump-schema', 'dump_schema')
options.add('-dump-migration', 'dump_migration')

options.execute()
