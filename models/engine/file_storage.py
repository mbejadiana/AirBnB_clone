#!/usr/bin/python3

"""
    Class FileStorage serializes instances to a JSON
    file and deserializes JSON file to instances
"""

import json
import os.path
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """"Class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Save a new object in the __objects dictionary"""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Convert the object into a dictionary and save it in the json file"""
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as a:
            new = {}
            for key, value in FileStorage.__objects.items():
                new[key] = value.to_dict()
            txt = json.dumps(new)
            a.write(txt)

    def reload(self):
        """Recharge information from json file and convert to an object"""

        my_dict = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Review': Review}
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as q:
                other_dict = json.loads(q.read())
                for key, val in other_dict.items():
                    self.new(my_dict[val['__class__']](**val))
