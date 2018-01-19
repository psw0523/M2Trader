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

여기 있는 코드를 우선 쭉 살펴본다.
### https://github.com/dennybritz/reinforcement-learning

### Introduction

1장을 보고 아래 사이트의 코드를 보고 돌려본다.
http://incompleteideas.net/book/bookdraft2018jan1.pdf
https://github.com/ShangtongZhang/reinforcement-learning-an-introduction/tree/master/chapter01

http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/intro_RL.pdf
https://gym.openai.com/docs

#### Reinforcement Learning: An Introduction Chapter 1. Introduction
Learning from interaction
Computational approach to learning from interaction.
##### 1.1 Reinforcement Learning
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

