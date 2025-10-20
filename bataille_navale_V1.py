#!/usr/bin/env python
# -*- coding: utf-8 -*-

def create_boat( letter_start, nb_start, letter_end, nb_end, name):
    """
    This function creates a boat with all occupied positions between two coordinates.
    :param letter_start: Starting column letter, example : "B"
    :param nb_start: Starting row letter, example : "2"
    :param letter_end: Ending column letter, example : "F"
    :param nb_end: Ending row number, example : "2"
    :param name: Name of the boat, example : "aircraft_carrier"
    :return: A list containing the boat's coordinates and its name, example : [['B2', 'C2', 'D2', 'E2', 'F2'], 'aircraft_carrier']
    """
    position_boat = []

    if letter_start != letter_end :
        for letters in range(ord(letter_start), ord(letter_end)+1):
            coordinates = chr(letters)+str(nb_start)
            position_boat.append(coordinates)
    else:
        for nb in range(nb_start, nb_end+1):
            coordinates = letter_start + str(nb)
            position_boat.append(coordinates)

    boat = [position_boat, name]
    return boat


def grid_boat_sample():
    """
    Creates and returns a sample grid containing predefined boat positions.
    :return: A list of boats, each represented as [positions, name].
    Example : [
                 [['B2', 'C2', 'D2', 'E2', 'F2'], 'aircraft_carrier'],
                 [['A4', 'A5', 'A6', 'A7'], 'cruiser'],
                 ...
             ]
    """
    grid = [create_boat("B",2, "F", 2, "aircraft_carrier"),
            create_boat("A",4, "A", 7, "cruiser"),
            create_boat("H", 5, "J", 5, "destroyer"),
            create_boat("C", 5, "C", 7, "submarine"),
            create_boat("E", 9, "F", 9, "torpedo_boat")]
    """grid = [create_boat("E", 9, "F", 9, "torpedo_boat")]"""
    return grid


def get_user_attack():
    """
    Prompts the user to enter the coordinates of their attack.
    :return: Example : "A4"
    """
    user_input = input("coordonnées du tir : ")
    while not verify_input(user_input):
         print("coordonnées incorrectes, recommencez")
         user_input = input("coordonnées du tir : ")
    return user_input


def verify_input(user_input):
    """
    Check if the user input is valid.
    A letter from 'A' to 'J'
    A number between 1 and 10
    :param user_input: the input string to validate
    :return: True if the input is valid, False otherwise
    """
    letter = user_input[0]
    nb = user_input[1:]

    if len(user_input)<2:
        return False
    if "A" <= letter <= "J" and 1 <= int(nb) <= 10:
        return True
    else:
        return False


def is_hit(grid_boat, position_attack):
    """
    Check if the user's attack hits a boat.
    If the position is found, it is removed from the boat's positions list.
    :param grid_boat: List of boats. Each boat is [positions, name]
    :param position_attack: Position targeted by the user, example: "A4"
    :return: True if a boat is hit, False if nothing is hit
    """
    for boat in grid_boat:
        if position_attack in boat[0]:
            boat[0].remove(position_attack)
            return True
    return False


def is_sunk(grid_boat):
    """
    Checks if any boat has been completely hit (sunk).
    If a boat has no remaining positions, it is removed from the grid.
    :param grid_boat: List of boats. Each boat is [positions, name]
    :return: True if a boat was sunk and removed, False otherwise
    """
    for boat in grid_boat:
        if not boat[0]:
            grid_boat.remove(boat)
            return True
    return False


def apply_attack(grid_boat, position_attack):
    """
    Apply the user's attack to the grid of boats.
    This function checks if the attack hits a boat, sinks it, or misses.
    It also displays a message to the user depending on the result.

    :param grid_boat: The list of boats (each boat is [positions, name])
    :param position_attack: The position attacked by the user, example : "A4"
    :return: The updated grid_boat after the attack
    """
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if is_hit(grid_boat, position_attack):
        if is_sunk(grid_boat):
            if not grid_boat:
                print("Toute la flotte est à l'eau, Vous avez gagné !!! Bravo")
                print("Fin du jeu")
            else:
                print("bateau coulé")
        else:
            print("bateau touché")
    else:
        print("missile à l'eau")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return grid_boat


def display_user_attacks(attacks_array, grid_boat):
    """
    Displays the game grid with the user's previous attacks.
    This function modifies the grid by calling is_hit(), which removes positions.
    :param attacks_array: List of positions attacked by the user, example : ["A4", "A2"]
    :param grid_boat: Current grid of boat (used to check hits)
    :return: None
    """
    print("    +---+---+---+---+---+---+---+---+---+---+")
    print("    |", end="")

    # Column headers: A to J
    for letter in range(ord("A"),ord("J")+1):
        print(f" {chr(letter)} |", end="")
    print("")
    print("+---+---+---+---+---+---+---+---+---+---+---+")

    # Rows 1 to 10
    for row_nb in range(1, 11):
        print(f"|{row_nb:3}|", end="")
        for col in range(10):
            col_letter = chr(ord('A') + col)
            col_row_position = f"{col_letter}{row_nb}"
            if col_row_position in attacks_array:
                if is_hit(grid_boat, col_row_position):
                    print(" X |", end="")
                else:
                    print(" 0 |", end="")
            else:
                print("   |", end="")

        print("")

    print("+---+---+---+---+---+---+---+---+---+---+---+")


if __name__ == '__main__':

    print("Début de la bataille navale : ")
    boat_grid = grid_boat_sample()
    continue_playing = "oui"
    user_attacks_list = []

    while continue_playing != "non":
        user_attack = get_user_attack()
        boat_grid = apply_attack(boat_grid, user_attack)
        user_attacks_list.append(user_attack)
        display_user_attacks(user_attacks_list, grid_boat_sample())
        if boat_grid:
            continue_playing = str(input("voulez-vous continuer ? "))
        else:
            continue_playing = "non"


    # prévoir un random de ces positions à venir
    # dans le cas d'un random une case ne peut pas être occupée par 2 bateaux
    # position verticale ou horizontale
