-- THis is a script to set up the database
-- of the Database

CREATE USER "hbnb_test"@"localhost" IDENTIFIED BY "hbnb_test_pwd"
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
GRANT ALL ON hbnb_test_db.* TO "hbnb_test"@"localhost";
GRANT SELECT ON performance_schema.* TO "hbnb_test"@"localhost";

FLUSH PRIVILEGES;
