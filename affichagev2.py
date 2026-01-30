import matplotlib.pyplot as plt
import numpy as np
from classes import *
from constantes import *
from map import *

def display_map(grid): # J'ai renommé 'map' en 'grid' car map est un mot clé Python
    GRID_SIZE = len(grid)
    # 1. Préparation du fond (Image)
    img = np.zeros((GRID_SIZE, GRID_SIZE, 3), dtype=np.uint8)
    
    # 2. Préparation des listes de coordonnées (Méthode Ingénieur)
    # Au lieu de dessiner 1 par 1, on note toutes les positions d'abord
    sheep_x, sheep_y = [], []
    wolf_x, wolf_y = [], []

    for y in range(GRID_SIZE):      # i correspond à y (lignes)
        for x in range(GRID_SIZE):  # j correspond à x (colonnes)
            cell = grid[y][x]       # Attention à la structure : cell est-elle une liste ou un objet ?
            
            # Adapte ces accès selon ta structure réelle (liste [grass, animal] ou objet Cell)
            grass_obj = cell[0] 
            animal_obj = cell[1]

            # --- Remplissage du fond ---
            if grass_obj is not None and grass_obj.state: # Si herbe présente
                img[y, x] = [34, 139, 34]  # ForestGreen
            else:
                img[y, x] = [139, 69, 19]  # SaddleBrown

            # --- Tri des animaux ---
            if isinstance(animal_obj, Sheep):
                sheep_x.append(x) # Attention : scatter prend (X, Y) donc (colonne, ligne)
                sheep_y.append(y)
            elif isinstance(animal_obj, Wolf):
                wolf_x.append(x)
                wolf_y.append(y)

    # 3. Affichage (Dans le bon ordre !)
    plt.figure(figsize=(6, 6)) # Optionnel : fixe la taille
    
    # D'ABORD le fond
    plt.imshow(img) 
    
    # ENSUITE les animaux (en un seul appel par espèce = beaucoup plus rapide)
    # zorder=2 assure qu'ils sont bien dessinés PAR DESSUS l'image
    if sheep_x: # On vérifie qu'il y a des moutons pour éviter une erreur
        plt.scatter(sheep_x, sheep_y, c='white', marker='x', s=100, label='Moutons', zorder=2)
    
    if wolf_x:
        plt.scatter(wolf_x, wolf_y, c='black', marker='x', s=100, label='Loups', zorder=2)

    plt.legend(loc='upper right') # Petit bonus : la légende
    plt.axis('off')
    plt.title("Simulation Écosystème")
    plt.show()

grid= create_map( GRID_SIZE, INITIAL_SHEEP, INITIAL_WOLVES, INITIAL_GRASS_COVERAGE)
display_map(grid)