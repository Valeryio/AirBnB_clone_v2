#!/usr/bin/env python3

import os
from sqlalchemy import *


username = "root"
password = "Val_Ery28!"
host = "localhost"
port = 3306
db_name = "NEW_DB_DAMN"

# os.environ["SQLALCHEMY_SILENCE_UBER_WARNING"] = "1"
os.system("export SQLALCHEMY_SILENCE_UBER_WARNING=1")
engine = create_engine(f"mysql://{username}:{password}@{host}:{port}")
engine.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
