'''
@author: job4
@creation_date: Feb 22, 2019
'''

from probability import JointProbDist, enumerate_joint_ask

P = JointProbDist(['Coin1', 'Coin2'])
Heads, Tails = True, False
P[Heads, Heads] = .25; P[Heads, Tails] = .25;
P[Tails, Heads] = .25; P[Tails, Tails] = .25;

PC = enumerate_joint_ask('Coin2', {'Coin1': Heads}, P)
print(PC.show_approx())

#The answer confirms what is generally believed about flipping coins.