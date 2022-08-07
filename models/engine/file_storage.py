#!/usr/bin/python3
"""Defines class that Stores first object"""
import json

class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances

    
    Attributes:
        __file_path (str): string - path to the JSON file 
        __objects (dict): A dictionary that will store all objects
    """


    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj
    
    def save(self):
        """serializes __objects to the JSON file"""
        dictionary = {}
        for key in self.__objects:
            dictionary[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictionary, f)
    
    def reload(self):
        """deserializes the JSON file to __objects, only if it exists"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass
