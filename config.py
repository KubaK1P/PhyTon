import json


class Config:
    def __init__(self):
        with open("config.json", "r") as f:
            self.__conf = json.load(f)

    def get(self, key: str):
        obj = self.__conf
        for k in key.split("."):
            obj = obj[k]
        return obj


config = Config()
