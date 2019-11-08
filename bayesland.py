#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:24:39 2019

@author: quzair

Agents walk around with boards listing things on which the ywould place a bet.
If they meet a person whose odds on an event differs substantially from their own odds on that event, then the two will make a bet
    if(abs(my_odds-their_bet)>threshold) make bet

- 3 agents bet on a probability of coin coming heads
- Coin simulated through a bernoulli process (prob of head is 60%)

Beginning of each round, an agent initializes

- a key (random integer 1-5)
- a hypothesis regarding the prob of heads
- Some kind of idea of past events
- A bankroll ~ 100

"""
import random
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt


class Agent(object) :
    def __init__(self, name, hypothesis_prob, index, bank):
        self.hypothesis_prob = scipy.stats.uniform(0,1).rvs()
        self.index = index
        self.bank = bank
        self.past_evnts = 0
        self.name = name
        self.bet = bank * 0.05

    def print_index(self):
        print(self.name + ": " + str(self.index))

    def update_agent(self):
        ind = random.randint(1,5)
        self.bet = self.bank * 0.05
        self.index = ind
        
    def hypothesis(self):
        return scipy.stats.uniform(0,1).rvs()
        
    
class Model(object):
    def __init__(self, agent1, agent2, agent3):
        self.agent1 = agent1
        self.agent2 = agent2
        self.agent3 = agent3
        self.coin = 1
        self.agents = [agent1,agent2,agent3]
        self.A,self.B,self.C = list(),list(),list()

    def coin_flip(self):
        return 1 if random.random() < 0.6 else 0  

    def run_model(self): 
        for x in range(1,15):
            print("----------------------")
            self.create_agents_index()
            self.print_agents_index()
            matched = self.check_same_index()
            print(matched)
            self.run_bets(matched)
            
            
    def check_same_index(self):
        matched = []
        for i in range(0,3):
            for j in range(i+1,3):
                print(self.agents[i].index)
                print(self.agents[j].index)
                if(self.agents[i].index is self.agents[j].index):
                    matched.append((i,j))
        return matched
    
    def run_bets(self, matched):
        if(len(matched)>0):
            for pair in matched:
                agent1 = self.agents[matched[0][0]]
                agent2 = self.agents[matched[0][1]]
                h1 = agent1.hypothesis()
                h2 = agent2.hypothesis()
                print(agent1.name)
                print(h1)
                print(agent2.name)
                print(h2)
                flip = self.coin_flip()
                print("coin " + str(flip))
                
                
                if np.abs(h1-h2) > 0.001 :
                    print("Before bet " + str(agent1.bet) + " " + str(agent2.bet)) 
                    bet = np.mean([agent1.bet,agent2.bet])
                    print("Bet " + str(bet))
                    if bet > agent1.bank:
                        bet = agent1.bank
                    if bet >agent2.bank:
                        bet = agent2.bank
                    
                    if h1 > h2 :
                        head = agent1
                        tail = agent2
                    else :
                        head = agent2
                        tail = agent1
                    
                    if flip == 1:
                        head.bank += bet
                        tail.bank -= bet
                    elif flip == 0:
                        head.bank -= bet
                        tail.bank += bet
                    
                    print("After bet" + str(agent1.bank) + " " + str(agent2.bank))
                else :
                    print("Not significant Difference in hypothesis")
        print(self.agent1.hypothesis_prob)
        print(self.agent1.bank)
        
        self.A.append([self.agent1.hypothesis_prob,self.agent1.bank])
        self.B.append([self.agent2.hypothesis_prob,self.agent2.bank])
        self.C.append([self.agent3.hypothesis_prob,self.agent3.bank])
            

    def create_plot(self):
        print(np.array(self.A).T)
        print(np.array(self.B).T)
        print(np.array(self.C).T)
        
        A = np.array(self.A).T
        B = np.array(self.B).T
        C = np.array(self.C).T
        
        fig,axs = plt.subplots(2,1)
        axs[0].set_ylabel("Prediction")
        axs[0].plot(A[0])
        axs[0].plot(B[0])
        axs[0].plot(C[0])
        axs[0].set_ylim(0,1)
        
        axs[1].set_ylabel("BankRoll")
        axs[1].plot(A[1])
        axs[1].plot(B[1])
        axs[1].plot(C[1])
        
        plt.show()
        
 
    def print_agents_index(self):
        for agent in self.agents:
            agent.print_index()
            
    def create_agents_index(self):
        for agent in self.agents:
            agent.update_agent()

if __name__ == '__main__':
    agent1 = Agent('Ag1ent',0.1,1,100)
    agent2 = Agent('Ag2ent',0.3,2,100)
    agent3 = Agent('Ag3ent',1,3,100)
    
    print("--------Start Model-------")
    
    model = Model(agent1,agent2,agent3)
    model.run_model()
    model.create_plot()


