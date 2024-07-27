-- THis script prepare a new database for
-- using it for the SQLAlchemy project
CREATE USER "hbnb_dev"@"localhost" IDENTIFIED BY "hbnb_dev_pwd";
CREATE DATABASE IF NOT EXISTS "hbnb_dev_db";
GRANT ALL ON hbnb_dev_db.* TO "hbnb_dev"@"localhost";
GRANT SELECT ON performance_schema TO "hbnb_dev"@"localhost";

FLUSH PRIVILEGES;
