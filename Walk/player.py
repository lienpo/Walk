from location import Location

class Player:

    def __init__(self, CURRENT_LOC):
        self.current = Location(CURRENT_LOC)

    def loc_and_routes(self):
        print("You are in " + self.current.name + "." + "\n")
        print("Where do you want to go?\n")
        self.current.print_all_neighbors()
