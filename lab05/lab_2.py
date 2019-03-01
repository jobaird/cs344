'''
This module implements the Bayesian network shown in Exercise 5.2
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
cancer = BayesNet([
    ('Cancer', '', .01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.20}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.20})
    ])

print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())
'''The results do make sense, even if they are a lot lower than one may expect. The result of one failed test has
a very large effect on the results of having cancer. The results are so low since the probability of having caner
in the first place is so small.'''