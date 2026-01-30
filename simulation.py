
from constantes import *
from classes import * 
from map import * 
import numpy as np 
import matplotlib.pyplot as plt 
from affichage import display_map

def simulation ():

    fini = False 
    time = 0 
    
    # on crée la grille
    grille = create_map( GRID_SIZE, INITIAL_SHEEP, INITIAL_WOLVES, INITIAL_GRASS_COVERAGE)

    while time <=  MAX_TURNS and not fini : 

        animal_alive = 0 

        for x in range(GRID_SIZE):
            for y in range (GRID_SIZE):
                
                # On augmente l'age des animaux 
                if grille[x,y][1] is not None :
                    animal = grille [x,y][1]
                    animal.age+=1

                    animal_alive+=1
                    

                    #vérification des morts : 

                    if animal.energy <= 0 : 
                        grille [x,y][1] = None 
                
                # On check l'état de l'herbe
                herbe = grille[x,y][0]

                # si on a déjà de l'herbe 
                if herbe.state : 
                    # si elle a été mangée depuis moins de 7 jours on augmente son temps de pousse 
                    if herbe.eaten and herbe.time_growth<7 :
                        herbe.time_growth +=1 
                    # mangée il y a 7 jours --> on met de l'herbe 
                    else : 
                        herbe.eaten = False
                        herbe.time_growth =0

                # Il n'y a pas d'herbe, on en crée aléatoirement 
                else : 
                    if np.random.random()<=GRASS_GROWTH_PROBABILITY :
                        grille[y,x][0]= Grass(True, False, 0) 
                
                if grille[x,y][1] is not None :
                    animal = grille [x,y][1]
                    # gestion  des montons 
                    if type(animal)== Sheep : 
                        if animal.age > SHEEP_MAX_AGE: 
                            grille [x,y][1] = None 
                        else : 
                            animal.move(grille)
                            animal.reproduction(grille)
                        
                        
                    # getsion des loups 

                    if type(animal)== Wolf : 
                        if animal.age > WOLF_MAX_AGE: 
                            grille [x,y][1] = None 
                        else : 
                            animal.move(grille)
                            animal.reproduction_wolf(grille)
                    # gestiond de l'arrêt 
        if animal_alive ==0 : 
            fini = True 
        time+=1
        print(time)
        #display_map(grille)

simulation()



                

                

                
                    
                
                


                





                

                

