#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    
    def __init__(self, name="", job=""):
        if job in APPROVED_JOBS:
            self.job = job
        else: 
            print("Job must be in list of approved jobs.")
        if isinstance(name, str):
            if name=="" or 1<len(name)>25:
                print("Name must be string between 1 and 25 characters.")
            else:
                self._name = name.title()
        else: print("Name must be string between 1 and 25 characters.")


    def get_name(self):
        return self._name
    
    def set_name(self, name=""):
        if isinstance(name, str):
            if name=="" or 1<len(name)>25:
                print("Name must be string between 1 and 25 characters.")
            else:
                self._name = name.title()
        else: print("Name must be string between 1 and 25 characters.")
    name = property(get_name, set_name)


guido = Person(name="", job="ITC")
print(guido.job)
    