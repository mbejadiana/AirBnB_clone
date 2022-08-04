#!/usr/bin/python3
""" 
Class FileStorage
"""
import json
import os

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
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as file_path:
            objects = json.load(file_path)
            FileStorage.__objects = {}
            for key in objects:
                name = key.split(".")[0]
                FileStorage.__objects[key] = my_dict[name](**objects[key])
