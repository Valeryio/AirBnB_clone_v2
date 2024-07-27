-- THis script prepare a new database for
-- using it for the SQLAlchemy project
CREATE USER "hbnb_dev"@"localhost" IDENTIFIED BY "hbnb_dev_pwd" IF NOT EXISTS "hbnb_dev";
CREATE DATABASE "hbnb_dev_db" IF NOT EXISTS "hbnb_dev_db";
GRANT ALL ON hbnb_dev_db.* TO "hbnb_dev"@"localhost";
GRANT SELECT ON performance_schema TO "hbnb_dev"@"localhost";

