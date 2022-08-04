#!/usr/bin/python3
""" 
Class FileStorage
"""
import json
import os.path

class FileStorage:
    """ Serializes instances to a JSON file and
    deserializes JSON file to instances"""
    _file_path = "file.json"
    _object = {}

    def all(self):
        """ Initializes class """
        return self._objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        obj = obj.__class__.__name__.obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
            with open(self.__file_path, 'w', encoding="UTF-8") as f:
                json.dump(my_dict, f)

    def reload(self):
        """ deserializes JSON file to _objects """
        if os.path.exists(FileStorage.__file_path):
            with open(self.__file_path) as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_d = obj["__class_"]
                    del obj["__class__"]
                    self.new(eval(cls_d)(**obj))
            return
