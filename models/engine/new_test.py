#!/usr/bin/env python3

import os
import MySQLdb


username = "root"
passwd = "Val_Ery28!"
host = "localhost"
port = 3306
db_name = "NEW_DB_DAMN"

db = MySQLdb.connect(host="localhost", user=username, password=passwd)
cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS PORN_IS_HORRIBLE")
