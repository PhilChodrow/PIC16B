from mesa.space import SingleGrid
from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import numpy as np

class SchellingAgent(Agent):
    
    # adding a pos instance variable so that each agent can remember
    # where they are. Note that the pos can take the place of the name. 
    def __init__(self, pos, agent_type, homophily, model):
        super().__init__(pos, model)
        self.pos = pos
        self.type = agent_type
        self.homophily = homophily
        
    
    def step(self):
        
        pct_similar_neighbors = np.mean([
            self.type == other.type for other in self.model.grid.neighbor_iter(self.pos)
        ])
        
        if pct_similar_neighbors < self.homophily:
            self.model.grid.move_to_empty(self)
            self.model.moved += 1   
        
class SchellingModel(Model):
    
    # need to specify width, height, and density of agents
    # in the grid. 
    def __init__(self, width, height, density, homophily):
        
        self.schedule = RandomActivation(self)
        
        # create the grid
        self.grid = SingleGrid(width, height, torus=True)
        
        self.moved = 0
        self.running = True
        
        # loop through the grid, and add agents so that the 
        # overall density is roughly equal to the passed 
        # density
        for cell in self.grid.coord_iter():
            x = cell[1]
            y = cell[2]
            if self.random.random() < density:
                
                agent_type = np.random.choice(["Orange", "Blue"])
                
                agent = SchellingAgent(pos = (x, y), 
                                 agent_type = agent_type, 
                                 homophily = homophily, 
                                 model = self)
                
                self.schedule.add(agent)    
                self.grid.position_agent(agent, (x, y))
        
        # NEW: create data collector
        self.datacollector = DataCollector(model_reporters={"num_moved": lambda m: m.moved},
                                       agent_reporters = {"x"      : lambda a: a.pos[0],
                                                          "y"      : lambda a: a.pos[1],
                                                          "type"   : lambda a: a.type})
        
    # this doesn't change, except that we will add a counter for the number of happy agents
    # who don't move in this timestep
    def step(self):
        self.moved = 0
        self.schedule.step()
        print(f"{self.moved} agents moved in this timestep")
        
        # NEW: call the data collector after each step
        self.datacollector.collect(self)
        
        self.running = self.moved != 0
        
    