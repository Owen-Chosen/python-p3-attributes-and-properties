#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:

    def __init__(self, name="", breed=""):
        if name == "" or type(name) in (int,float) or len(name)>25:
            print("Name must be string between 1 and 25 characters.")
        if breed in APPROVED_BREEDS == False:
            print("Breed must be in list of approved breeds.")
        else:
            self._name = name
            self._breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if name == "" or type(name) in (int,float) or len(name)>25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed=""):
        if breed in APPROVED_BREEDS:
            self._breed = breed

    breed = property(get_breed, set_breed)