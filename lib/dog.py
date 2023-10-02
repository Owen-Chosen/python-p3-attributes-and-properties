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
    def __init__(self):
        self._name = ""

    def get_name(self):
        return self._name

    def set_name(self, name):
        if(type(name) in str and (1 <= len(name) <= 25)):
            self._name = name

    name = property(get_name, set_name)
