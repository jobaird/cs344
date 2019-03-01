'''
This module implements the Bayesian network shown in Exercise 5.3
It's taken from the AIMA Python code.

@author: kvlinden
@edited_by:Job4
@version Jan 2, 2013
@edited_on March 1, 2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
happy = BayesNet([
    ('Sunny', '', .7),
    ('Raise', '', .01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.70, (F, T): 0.90, (F, F): 0.10})
    ])

print(enumeration_ask('Raise', dict(Sunny=T), happy).show_approx())
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happy).show_approx())

print(enumeration_ask('Raise', dict(Happy=T), happy).show_approx())
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())
'''The results mostly make sense. Since we know he is already happy, if we know that it isn't because its sunny then
there is a better chance that he got a raise, given that he is happy.'''