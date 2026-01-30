# je veux afficher la map de create_map dans map.py 
import matplotlib.pyplot as plt
import numpy as np  
# je veux que les cases avec de l'herbe soient en vert,
# celles sans herbe en marron, les moutons en croix blanche et les loups en croix noir
from classes.py import * 
from map.py import * 
from constantes.py import *



def display_map(map):
    GRID_SIZE = len(map)
    img = np.zeros((GRID_SIZE, GRID_SIZE, 3), dtype=np.uint8)

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            grass = map[i][j][0]
            animal = map[i][j][1]

            # Définir la couleur de fond en fonction de l'herbe
            if grass is not None and grass.state:
                img[i, j] = [34, 139, 34]  # Vert pour l'herbe
            else:
                img[i, j] = [139, 69, 19]  # Marron pour pas d'herbe

            # Ajouter les animaux
            if isinstance(animal, Sheep):
                plt.scatter(j, i, color='white', marker='x')  # Mouton en croix blanche
            elif isinstance(animal, Wolf):
                plt.scatter(j, i, color='black', marker='x')  # Loup en croix noire

    plt.imshow(img)
    plt.axis('off')
    plt.show()






map = create_map(GRID_SIZE, INITIAL_SHEEP, INITIAL_WOLVES, INITIAL_GRASS_COVERAGE)