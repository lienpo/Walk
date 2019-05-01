import os

class Location:

    def __init__(self, NAME):
        self.name=NAME
        self.neighbors = []

        self.give_all_neighbors()

    def give_all_neighbors(self):
        file_loc = "Locations/" + self.name + ".txt"
        with open(file_loc) as f:
            self.neighbors = f.readlines()

    def print_all_neighbors(self):
        for neighbor in self.neighbors:
            print neighbor
