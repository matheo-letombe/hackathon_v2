from map import map
import random as rd
class Grass:
    def __init__(self, state:bool, eaten:bool, time_growth:int):
        self.state = state 
        self.eaten = eaten
        self.time_growth = time_growth


class Animal:
    position:tuple
    age:int
    energy:int

    def move_right_possible(self) -> bool:
        return self.position[0] < map.length
    
    def move_right(self):
        if self.move_right_possible():
            self.position[0] += 1
        else:
            return False
    
    
    def move_left_possible(self) -> bool:
        return self.position[0] > 0
    
    def move_left(self):
        if self.move_left_possible():
            self.position[0] += -1
        else:
            return False


    def move_up_possible(self):
        return self.position[1] < map.length
    
    def move_up(self):
        if self.move_up_possible():
            self.position[1] += 1
        else:
            return False
    
    
    def move_down_possible(self):
        return self.position[1]>0
    
    def move_down(self):
        if self.move_down_possible():
            self.position[1] += -1
        else: 
            return False

class Sheep(Animal):
    def move(self)->None:
        if self.move_down_possible() and map[self.position[0]][self.position[1]-1][0].state :
            self.move_down()
            self.eat_grass()
        if self.move_up_possible() and map[self.position[0]][self.position[1]+1][0].state:
            self.move_up()
            self.eat_grass()
        if self.move_right_possible() and map[self.position[0]+1][self.position[1]][0].state:
            self.move_right()
            self.eat_grass()
        if self.move_left_possible() and map[self.position[0]-1][self.position[1]][0].state:
            self.move_left()
            self.eat_grass()
        else:
            L = [self.move_down(), self.move_up(), self.move_left(), self.move_right()]
            for i in range(4,0,-1):
                r = rd.randint(0,i)
                if L[r] != False:
                    L[r]
                    break
                else:
                    L.remove(L[r])
            
    def eat_grass(self) -> None:
        herbe = map[self.position[0]][self.position[1]][0]
        herbe.eaten = True
        herbe.time_growth = 0
        self.energy += 20   
               
class Wolf(Animal):
    pass
