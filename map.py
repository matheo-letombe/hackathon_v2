# création de la map 
import numpy as np 
import random as rd 
from constantes import *
from classes import Grass, Sheep, Wolf



def create_map( GRID_SIZE, INITIAL_SHEEP, INITIAL_WOLVES, INITIAL_GRASS_COVERAGE):
    map = np.array([[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)], dtype=object)
    # Initialiser la couverture d'herbe
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE): 
            # l'emplacement 0 de la liste correspond à l'herbe, le 1 au mouton ou au loup
            map[i][j] = [Grass(False, False, 0), None]

            # on définit une probabilité pour chaque case d'avoir de l'herbe, un mouton ou un loup
            r_grass = rd.random() 
            r_sheep = rd.random()
            r_wolf = rd.random()

            # on initialise l'herbe, les moutons et les loups en fonction des probabilités
            if r_grass < INITIAL_GRASS_COVERAGE:
                map[i][j][0] = Grass(True, False, 0)
            else : 
                map[i][j][0] = Grass(False, False, 0)

            if r_sheep < INITIAL_SHEEP / (GRID_SIZE * GRID_SIZE):
                map[i][j][1] =  Sheep((j,i), 0, SHEEP_INITIAL_ENERGY)
            # il n'y a pas de mouton à cet endroit


            elif r_wolf < INITIAL_WOLVES / (GRID_SIZE * GRID_SIZE):
                map[i][j][1] = Wolf((j,i), 0, WOLF_INITIAL_ENERGY)
            
            else : 
                map[i][j][1] = None

    return map

