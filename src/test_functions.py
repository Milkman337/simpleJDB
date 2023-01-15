import unittest
import os
import simpleJDB

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Remove the database file before running the test cases
        if os.path.isfile("testdb.json"):
            os.remove("testdb.json")
        self.db = simpleJDB.database("testdb")


    def test_setkey(self):
        self.db.setkey("key1", "value1")
        self.db.commit()
        self.assertEqual(self.db.getkey("key1"), "value1")
        self.assertEqual(self.db.gettype("key1"), "str")
        self.db.setkey("key1", 1)
        self.db.commit()
        self.assertEqual(self.db.getkey("key1"), 1)
        self.assertEqual(self.db.gettype("key1"), "int")

    def test_delkey(self):
        self.db.setkey("key1", "value1")
        self.db.delkey("key1")
        self.db.commit()
        self.assertRaises(TypeError, self.db.getkey, "key1")
        self.assertRaises(TypeError, self.db.delkey, "key1")

    def test_getkey(self):
        self.db.setkey("key1", "value1")
        self.db.commit()
        self.assertEqual(self.db.getkey("key1"), "value1")
        self.assertRaises(TypeError, self.db.getkey, "key2")

    def test_gettype(self):
        self.db.setkey("key1", "value1")
        self.db.commit()
        self.assertEqual(self.db.gettype("key1"), "str")
        self.assertRaises(TypeError, self.db.gettype, "key2")

    def tearDown(self):
        # Re-create the database file after the test cases have been executed
        with open("testdb.json", "w") as f:
            f.write("{\"main\": []}")

if __name__ == '__main__':
    unittest.main()
