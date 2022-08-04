#!/usr/bin/python3

"""
    Class FileStorage serializes instances to a JSON
    file and deserializes JSON file to instances
"""

import json
import os.path as path
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """"Class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects"""
        return self.__objects

    def new(self, obj):
        """Save a new object in the __objects dictionary"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Convert the object into a dictionary and save it in the json file"""
        with open(self.__file_path, mode="w", encoding="UTF-8") as a:
            new = {}
            for key, value in self.__objects.items():
                new[key] = value.to_dict()
            txt = json.dumps(new)
            a.write(txt)

    def reload(self):
        """Recharge information from json file and convert to an object"""
        if (path.isfile(self.__file_path)):
            with open(self.__file_path, encoding="UTF-8") as a:
                txt = a.read()
            if(len(txt) > 0):
                dic = json.loads(txt)
                for key, value in dic.items():
                    obj = eval(value["__class__"])(**value)
                    self.__objects[key] = obj
