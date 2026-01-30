from map import map
import random as rd
class Grass:
    def __init__(self, state:int, eaten:bool, time_growth:int):
        self.state = state 
        self.eaten = eaten
        self.time_growth = time_growth
class Animal:
    position:tuple
    age:int
    energy:int

    def move_right_possible(self) -> bool:
        return self.position < map.length
    def move_right(self):
        self.position[0] += 1
    def move_left(self):
        self.position[0] += -1
    def move_up(self):
            self.position[1] += 1
    def move_down(self):
        self.position[1] += -1

class Sheep(Animal):
    def move(self)->None:
        
            
                
               
class Wolf(Animal):
    pass
