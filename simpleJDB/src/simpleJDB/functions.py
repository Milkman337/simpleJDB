import json

class database:
    def __init__(self, name: str) -> None:
        self.name = name
        try:
            with open(f"{self.name}.json", "r") as f:
                self.data = json.load(f)
        except:
            with open(f"{self.name}.json", "w") as f:
                f.write("{\"main\": {}}")
            with open(f"{self.name}.json", "r") as f:
                self.data = json.load(f)

    def setkey(self, keyname: str, value):
        gk = 0
        for thing in self.data["main"]:
            if thing["keyname"] == keyname:
                thing["value"] = value
                gk = 1
                with open(f"{self.name}.json", "w") as f:
                    json.dump(self.data, f)
        if gk == 0:
            self.data["main"].append({"keyname": keyname, "value": value})
            with open(f"{self.name}.json", "w") as f:
                json.dump(self.data, f)

    def delkey(self, keyname:str):
        for thing in self.data["main"]:
            if thing["keyname"] == keyname:
                self.data["main"].remove(thing)
                with open(f"{self.name}.json", "w") as f:
                    json.dump(self.data, f)
        raise TypeError("Key has not been found.")

    def gettype(self, keyname:str):
        for thing in self.data["main"]:
            if thing["keyname"] == keyname:
                return type(thing["value"])
        raise TypeError("Key has not been found.")