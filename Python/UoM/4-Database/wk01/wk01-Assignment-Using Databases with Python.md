Assignment - Using Databases with Python
========================================

Instructions
------------
First, create a SQLITE database or use an existing database and then create a table in the database called "Ages":

```SQL
CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)
```

Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:

~~~SQL
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Laibah', 23);
INSERT INTO Ages (name, age) VALUES ('Elyan', 27);
INSERT INTO Ages (name, age) VALUES ('Wardah', 38);
INSERT INTO Ages (name, age) VALUES ('Chibudom', 20);
INSERT INTO Ages (name, age) VALUES ('Clarke', 19);
INSERT INTO Ages (name, age) VALUES ('Rosalie', 26);
```

Once the inserts are done, run the following SQL command:

```SQL
SELECT hex(name || age) AS X FROM Ages ORDER BY X
```

Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.