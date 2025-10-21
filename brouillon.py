def ship_is_hit(self, shot_coord):
    return shot_coord in self.position.keys()


def ship_is_sunk(self):
    return not any(self.position.values())


class Fleet:
    def __init__(self):
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)


new_fleet = Fleet()
for ship in Ship.boats:
    new_fleet.add_ship(ship)

print(new_fleet.ships[1])

"""for boat in Ship.boats:
    print(f"{boat.name}")"""

#print(Ship.ship_is_hit("E1"))