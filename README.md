# bayesland
Agent Based Modeling for Bayesland


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

