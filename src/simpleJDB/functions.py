import json
import threading

class database:
    """
    A class representing a database using json files.

    Attributes:
        name (str): The name of the json file.
        data (dict): The data stored in the json file.
    """
    def __init__(self, name: str) -> None:
        """
        Initialize the database with the given name.

        Args:
            name (str): The name of the json file.

        Returns:
            None
        """
        self.name = name
        try:
            with open(f"{self.name}.json", "r") as f:
                self.data = json.load(f)
                self.staged_data = self.data.copy()
        except:
            with open(f"{self.name}.json", "w") as f:
                f.write("{\"main\": []}")
            with open(f"{self.name}.json", "r") as f:
                self.data = json.load(f)
                self.staged_data = self.data.copy()
        self.lock = threading.Lock()


    def setkey(self, keyname: str, value) -> None:
        """
        Add or update a keyname and its value in the json file.

        Args:
            keyname (str): The keyname to add or update.
            value: The value associated with the keyname.

        Returns:
            None
        """
        with self.lock:
            data_type = type(value).__name__
            gk = 0
            for thing in self.staged_data["main"]:
                if thing["keyname"] == keyname:
                    thing["value"] = value
                    thing["datatype"] = data_type
                    gk = 1
            if gk == 0:
                self.staged_data["main"].append({"keyname": keyname, "value": value, "datatype": data_type})


    def delkey(self, keyname:str) -> None:
        """
        Delete a keyname and its value from the json file.

        Args:
            keyname (str): The keyname to delete.

        Returns:
            None

        Raises:
            TypeError: If the keyname is not found in the json file.
        """
        with self.lock:
            for thing in self.staged_data["main"]:
                if thing["keyname"] == keyname:
                    self.staged_data["main"].remove(thing)
                    return
            raise TypeError("Key has not been found.")


    def gettype(self, keyname:str):
        """
        Get the data type of the value associated with a keyname.

        Args:
            keyname (str): The keyname to check.

        Returns:
            type: The data type of the value associated with the keyname.

        Raises:
            TypeError: If the keyname is not found in the json file.
        """
        with self.lock:
            for thing in self.data["main"]:
                if thing["keyname"] == keyname:
                    return thing["datatype"]
            raise TypeError("Key has not been found.")


    def getkey(self, keyname:str):
        """
        Get the value associated with a keyname.

        Args:
            keyname (str): The keyname to retrieve the value for.

        Returns:
            Any: The value associated with the keyname.

        Raises:
            TypeError: If the keyname is not found in the json file.
        """
        with self.lock:
            for thing in self.data["main"]:
                if thing["keyname"] == keyname:
                    return thing["value"]
            raise TypeError("Key has not been found.")


    def commit(self) -> None:
        """
        Writes the current state of the 'staged_data' attribute to the json file.
        
        Returns:
            None
        """
        with self.lock:
            self.data = self.staged_data.copy()
            with open(f"{self.name}.json", "w") as f:
                json.dump(self.data, f)
