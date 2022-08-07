#!usr/bin/python3
""" class file_storage """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ Clase file Storage"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ Init """
        pass

    def all(self):
        """ return __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Create a new instance """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """ Save function """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict.update({key: value.to_dict()})
        json_file = json.dumps(new_dict)
        with open(FileStorage.__file_path, "w") as my_file:
            my_file.write(json_file)

    def reload(self):
        """ Reload from JSON file """
        my_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}

        json_file = ""
        try:
            with open(FileStorage.__file_path, "r") as my_file:
                json_file = json.loads(my_file.read())
                for key in json_file:
                    FileStorage.__objects[key] = my_dict[json_file[key]['__clas\
s__']](**json_file[key])
        except:
            pass
