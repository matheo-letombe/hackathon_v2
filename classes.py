import random as rd
from constantes import*
import time
class Grass: #On définit la classe de l'herbe avec tous les paramètres demandés
    def __init__(self, state:bool, eaten:bool, time_growth:int):
        self.state = state 
        self.eaten = eaten
        self.time_growth = time_growth


class Animal: #On définit une classe mère Animal et tous les paramètres et foncitons communs à tous les animaux (déplacement, age, énergie, position)
    def __init__(self, position:tuple, age:int, energy:int):
        self.position = position
        self.age = age
        self.energy = energy

    def move_right_possible(self) -> bool: #On crée une fonction pour savoir si bouger à droite est possible
        return self.position[0] < GRID_SIZE #Possibilité de rajouter des lignes de code pour modéliser des obstacles
    
    def move_right(self, map):
        if self.move_right_possible():
            self.position[0] += 1 #On augmente la position en x pour aller à droite
            case = self.position
            map[case[1]][case[0]][1] = self
        else:
            return False
    
    
    def move_left_possible(self) -> bool:
        return self.position[0] > 0
    
    def move_left(self, map):
        if self.move_left_possible():
            self.position[0] += -1
            case = self.position
            map[case[1]][case[0]][1] = self
        else:
            return False


    def move_up_possible(self):
        return self.position[1] > 0
    
    def move_up(self, map):
        if self.move_up_possible():
            self.position[1] -= 1
            case = self.position
            map[case[1]][case[0]][1] = self
        else:
            return False
    
    
    def move_down_possible(self):
        return self.position[1] < GRID_SIZE
    
    def move_down(self, map):
        if self.move_down_possible():
            self.position[1] += -1
            case = self.position
            map[case[1]][case[0]][1] = self
        else: 
            return False

class Sheep(Animal): #On définit la sous-classe mouton et les fonctions propres aux moutons
    def move(self, map)->None:
        case = self.position
        if self.move_down_possible() and map[case[1]+1][case[0]][0].state: #On regarde s'il est possible de bouger sur les cases adjacentes et si celles-ci ont de l'herbe
            self.move_down(map)
            self.eat_grass(map)
        if self.move_up_possible() and map[case[1]-1][case[0]][0].state:
            self.move_up(map)
            self.eat_grass(map)
        if self.move_right_possible() and map[case[1]][case[0]+1][0].state:
            self.move_right(map)
            self.eat_grass(map)
        if self.move_left_possible() and map[case[1]][case[0]-1][0].state:
            self.move_left(map)
            self.eat_grass(map)
        else:
            L = [self.move_down(map), self.move_up(map), self.move_left(map), self.move_right(map)]
            for i in range(4,0,-1): 
                r = rd.randint(0,i) #On choisit de manière aléatoire un mvt
                if L[r] != False: #Si le mouvement est possible, on bouge
                    break
                else: #Si le mvt n'est pas possible, on enlève le mvt des possibilités et on ré-itère le processus
                    L.remove(L[r])
        self.energy -= SHEEP_ENERGY_LOSS_PER_TURN
            
    def eat_grass(self, map) -> None:                                   #On définit la fonction pour manger de l'herbe
        herbe = map[self.position[1]][self.position[0]][0]
        if herbe.state:
            herbe.eaten = True                                         #On change le statut de l'herbe en place
            herbe.time_growth = 0                                      #On initialise le temps de repousse
            self.energy += SHEEP_ENERGY_FROM_GRASS                     #On augmente l'énergie du mouton
    
    def create_sheep(self, map) -> None: #On définit la fonction pour créer un mouton sur une case adjacente que l'on appellera dans la fonction reproduction
        case = self.position
        sheep = Sheep(case, 0, SHEEP_INITIAL_ENERGY)
        if case[1] > 0 and map[case[1]-1][case[0]][1] == None: #On regarde toutes les possibilités, par défaut on le fait dans cet ordre, possibilité de rendre le procédé aléatoire
            sheep.position[1] -= 1
            map[case[1]-1][case[0]][1] = sheep
            return True
        if case[1] < GRID_SIZE and map[self.position[1]+1][self.position[0]] == None:
            sheep.position[1] += 1
            map[case[1]+1][case[0]] = sheep
            return True
        if case[0] > 0 and map[self.position[1]][self.position[0]-1] == None:
            sheep.position[0] -= 1
            map[case[1]][case[0]-1] = sheep
            return True
        if case[0] < GRID_SIZE and map[case[1]][case[0]+1][1] == None:
            sheep.position[0] += 1
            map[case[1]][case[0]+1][1] = sheep
            return True
        else:
            print("Le mouton ne peut pas se reproduire !")
            return False
            
    
    def reproduction(self, map) -> None: #On définit la fonction reproduction
        if self.energy >= SHEEP_REPRODUCTION_THRESHOLD and self.create_sheep(map):
            self.energy -= REPRODUCTION_ENERGY_COST #On enlève l'énergie qui a servi à se reproduire

class Wolf(Animal):
    def move(self, map)->None:
        case = self.position
        if self.move_down_possible() and map[case[1]+1][case[0]][1] != None : #On regarde s'il est possible de bouger sur les cases adjacentes et si un mouton est situé sur celles-ci
            self.move_down(map)
            self.energy += WOLF_ENERGY_FROM_SHEEP
        if self.move_up_possible() and map[case[1]-1][case[0]][0] != None:
            self.move_up(map)
            self.energy += WOLF_ENERGY_FROM_SHEEP
        if self.move_right_possible() and map[case[1]][case[0]+1][0] != None:
            self.move_right(map)
            self.energy += WOLF_ENERGY_FROM_SHEEP
        if self.move_left_possible() and map[case[1]][case[0]-1][0] != None:
            self.move_left(map)
            self.energy += WOLF_ENERGY_FROM_SHEEP
        else:
            L = [self.move_down(map), self.move_up(map), self.move_left(map), self.move_right(map)]
            for i in range(4,0,-1): 
                r = rd.randint(0,i) #On choisit de manière aléatoire un mvt
                if L[r] != False: #Si le mouvement est possible, on bouge
                    break
                else: #Si le mvt n'est pas possible, on enlève le mvt des possibilités et on ré-itère le processus
                    L.remove(L[r])
        self.energy -= WOLF_ENERGY_LOSS_PER_TURN

    
    def create_wolf(self, map) -> None: #On définit la fonction pour créer un loup sur une case adjacente que l'on appellera dans la fonction reproduction
        case = self.position
        wolf = Wolf(case, 0, SHEEP_INITIAL_ENERGY)
        if case[1] > 0 and map[case[1]-1][case[0]][1] == None: #On regarde toutes les possibilités, par défaut on le fait dans cet ordre, possibilité de rendre le procédé aléatoire
            wolf.position[1] -= 1
            map[case[1]-1][case[0]][1] = wolf
            return True
        if case[1] < GRID_SIZE and map[self.position[1]+1][self.position[0]] == None:
            wolf.position[1] += 1
            map[case[1]+1][case[0]] = wolf
            return True
        if case[0] > 0 and map[self.position[1]][self.position[0]-1] == None:
            wolf.position[0] -= 1
            map[case[1]][case[0]-1] = wolf
            return True
        if case[0] < GRID_SIZE and map[case[1]][case[0]+1][1] == None:
            wolf.position[0] += 1
            map[case[1]][case[0]+1][1] = wolf
            return True
        else:
            print("Le loup ne peut pas se reproduire !")
            return False
        
    