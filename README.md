 M2Trader
 --------

# Job list
- github repository setup --> Done
- PC remote working environment setup
- write kiwoom open api fake invest code
- write kiwoom open api get account state and get stock state
- writke zeromq server-client example code
- define state
- write M2Server
- write M2Env
- write PolicyEstimator
- write ValueEstimator
- write Reinforce and test(1st version)
- write ActorCritic and test(2nd version)
- write A3C and test(3rd version)
- select best model and optimize

# Reinforcement Learning Working Note
## Reference
### https://mpatacchiola.github.io/blog/
### https://github.com/dennybritz/reinforcement-learning
### https://github.com/reinforceio/tensorforce
### https://github.com/ShangtongZhang/reinforcement-learning-an-introduction
### Book Reinforcement Learning: An Introduction

## Repository
### git@github.com:psw0523/M2Trader.git

## 2018.01.16
### 마눌님이 작성한 code commit함
<pre><code>
$ git clone git@github.com:psw0523/M2Trader.git
$ git add envs/
$ git commit
$ git push origin master:master
</code></pre>

Reference Site
- http://incompleteideas.net/book/bookdraft2018jan1.pdf
- https://github.com/dennybritz/reinforcement-learning
- https://github.com/ShangtongZhang/reinforcement-learning-an-introduction/tree/master/chapter01
- http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/intro_RL.pdf
- https://gym.openai.com/docs

## Chapter 1. Introduction
Computational approach to learning from interaction.

### 1.1 Reinforcement Learning
learning how to map situations and actions so as to maximize reward signal.  
trial-and-error search and delayed reward.  
problem과solution method는 다른 관점이다.  

define problem  
using ideas from dynamical systems theory --> Markov Decision Process.
- Learnig Agent
- State of its environment
- Actions  

Third maching learning paradigm vs supervised, unsupervised  
Trade off between exploration and exploitation  
- exploit: 기존에 reward를 주는 action을 선택하는 것
- exploration: 더 나은 보상을 얻기 위하여 다른 action을 선택하는 것

### 1.2 Examples

### 1.3 Elements of Reinforcement Learnig
4 main subelements  
*policy, reward signal, value function, model of environment*  

#### policy
- mapping from states to actions
- maybe simple function or lookup table
- maybe stochastic

#### reward signal
- environment sends to agent the number called *reward* at each step
- primary base for altering the *policy*
- may be stochastic functions of state and actions taken

#### value function
- specifies what is good in the long run
- the value of state is total amount of reward an agent can expect to accumulate over the future, starting from that state
- state might always yield a low immediate reward but still have a high value becuase followed states yield high rewards
- Action choices are made based on value judgements
- Reward is given directly by environment but value must be estimated
- Value estimation function is most important thing about reinforcement learning

#### model of the environment
- mimics the behavior of the environment
- Given state, give next state and next reward
- used for planning
- model-based methods vs model-free methods

### 1.4 Limitations and Scope
- State is from MDP
- Don't focus state construction.
- Focus fully on decision-making issues
- Structured around estimating value functions
- Don't describe evolutionary methods(genetic algorithm)

### 1.5 An Extended Example; Tic-Tac-Toe
- Need All States Table: 3x3 matrix
- Need State Value Table
- Need algorithm for taking next action given current state
- Need algorithm for updating State Value Table by reward
- TicTacToe.py
