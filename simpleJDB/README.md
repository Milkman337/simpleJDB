# simpleJDB

simpleJDB is a simple python databse.

## Example Code

initialize the database:

    from simpleJDB.functions import database

    db = database("databsename")

to add a key

    value_to_add = 22

    db.setkey("keyname", 1)

to change the value of a key

    db.setkey("name of key you want to change", 2)

to delete a key

    db.delkey("key to delete")

to get a keys value

    db.getkey("key")

to get the type of a key

    db.gettype("key")