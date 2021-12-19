# simpleJDB

simpleJDB is a simple python databse.

## Example Code

initialize the database:
.. code-block:: python
    from simpleJDB.functions import database

    db = database("databsename")

to add a key
.. code-block:: python
    value_to_add = 22

    db.setkey("keyname", 1)

to change the value of a key
-- code-block:: python
    db.setkey("name of key you want to change", 2)

to delete a key
-- code-block:: python
    db.delkey("key to delete")

to get the type of a key
-- code-block:: python
    db.gettype("key")