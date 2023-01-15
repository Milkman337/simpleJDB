simpleJDB
=========

simpleJDB is a lightweight and easy-to-use python database that allows you to store, retrieve, and manipulate data with minimal code.

Features
--------

*   Support for multiple data types: simpleJDB supports storing integers, strings, floats, and lists as values.
*   Concurrency Support: simpleJDB is thread-safe and can handle simultaneous access and modification of data by multiple users.
*   Staging/Commit: simpleJDB has a staging/commit feature that allows you to make changes to the data before committing them to the json file.
*   Documentation: simpleJDB is well-documented and easy to understand, making it easier to get started with the library.
*   Unit testing: simpleJDB has a comprehensive test suite to ensure that the library is working as expected and to catch any bugs before they are released to the public.

Getting Started
---------------

To initialize the database, simply import the simpleJDB module and create a new database object, passing in a name for the database as an argument:

`import simpleJDB db = simpleJDB.database("my_database")`

Adding and Updating Keys
------------------------

To add a new key-value pair to the database, use the setkey() method and pass in the key name and the value to be stored:

`db.setkey("age", 22)`

You can also update the value of an existing key by calling setkey() with the same key name and a new value:

`db.setkey("age", 23)`

When you are ready to commit the changes to the json file, use the commit() method:

`db.commit()`

Retrieving and Deleting Keys
----------------------------

To retrieve the value of a key, use the getkey() method and pass in the key name:

`age = db.getkey("age")`

To delete a key, use the delkey() method and pass in the key name:

`db.delkey("age")`

Key Type
--------

To check the data type of a key, use the gettype() method and pass in the key name:

`data_type = db.gettype("age")`

Conclusion
----------

With simpleJDB, you can easily store and manipulate data in a pythonic way. With the added features, you can do more complex data manipulation and you can use it in a concurrent environment. Give it a try and see how it can simplify your project.