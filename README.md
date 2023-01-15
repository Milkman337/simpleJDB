simpleJDB
=========

simpleJDB is a lightweight and easy-to-use python database that allows you to store, retrieve, and manipulate data with minimal code.

Getting Started
---------------

To initialize the database, simply import the `simpleJDB` module and create a new `database` object, passing in a name for the database as an argument:

`import simpleJDB  db = simpleJDB.database("my_database")`

Adding and Updating Keys
------------------------

To add a new key-value pair to the database, use the `setkey()` method and pass in the key name and the value to be stored:

`db.setkey("age", 22)`

You can also update the value of an existing key by calling `setkey()` with the same key name and a new value:

`db.setkey("age", 23)`

Retrieving and Deleting Keys
----------------------------

To retrieve the value of a key, use the `getkey()` method and pass in the key name:

`age = db.getkey("age")`

To delete a key, use the `delkey()` method and pass in the key name:

`db.delkey("age")`

Key Type
--------

To check the data type of a key, use the `gettype()` method and pass in the key name:

`data_type = db.gettype("age")`

Conclusion
----------

With simpleJDB, you can easily store and manipulate data in a pythonic way. So, give it a try and see how it can simplify your project.