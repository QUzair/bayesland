#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:24:39 2019

@author: quzair
"""
import random

class Agent(object) :
    def __init__(self, name, hypothesis_prob, index,bankroll):
        self.hypothesis_prob = hypothesis_prob
        self.index = index
        self.bankroll = bankroll
        self.past_evnts = 0
        self.name = name

    def print_index(self):
        print(self.name + ": " + str(self.index))

    def create_random_index(self):
        ind = random.randint(1,5)
        self.index = ind
        
    def give_hypothesis(self):
        return 1 if random.random() < self.hypothesis_prob else 0 
        
    
class Model(object):
    def __init__(self, agent1, agent2, agent3):
        self.agent1 = agent1
        self.agent2 = agent2
        self.agent3 = agent3
        self.coin = 1
        self.agents = [agent1,agent2,agent3]

    def coin_flip(self):
        return 1 if random.random() < 0.6 else 0  

    def run_model(self): 
        for x in range(1,50):
            print("----------------------")
            self.create_agents_index()
            self.print_agents_index()
            print("coin " + str(self.coin_flip()))
            i = self.check_same_index()
            print(i)
            
            
    def check_same_index(self):
        for i in range(0,3):
            for j in range(i+1,3):
                print(self.agents[i].index)
                print(self.agents[j].index)
                if(self.agents[i].index is self.agents[j].index):
                    return i,j

        return -1
    
    def print_agents_index(self):
        for agent in self.agents:
            agent.print_index()
            
    def create_agents_index(self):
        for agent in self.agents:
            agent.create_random_index()

if __name__ == '__main__':
    agent1 = Agent('Ag1ent',0.1,1,100)
    agent2 = Agent('Ag2ent',0.3,2,100)
    agent3 = Agent('Ag3ent',0.5,3,100)
    
    model = Model(agent1,agent2,agent3)
    model.run_model()



"""
Agents walk around with boards listing things on which the ywould place a bet.
If they meet a person whose odds on an event differs substantially from their own odds on that event, then the two will make a bet
    if(abs(my_odds-their_bet)>threshold) make bet

- 3 agents bet on a probability of coin coming heads
- Coin simulated through a bernoulli process (prob of head is 60%)

Beginning of each round, an agent initializes

- a key (random integer 1-5)
- a hypothesis regarding the prob of heads
- Some kind of idea of past events
- A bankroll



"""