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
'''
P(Raise|Sunny) = alpha * <P(Raise|Sunny), P(-Raise|Sunny) = alpha * <.01 * .7,.99*.7> =
alpha * < .007,0.693> = <.007/(.007+.693),.0693/(.007*.693)> =
<.01,.99>
'''
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happy).show_approx())
'''
P(Raise|Happy^Sunny) = alpha * P(Raise) * P(Happy) * P(Happy|Raise,Sunny) =
alpha * <.01 * .07 * 1.0,.99 *.07*.07> = alpha * <.007,.4851> =
<.007/(.007+.4851),.4851/(.007+..4851)> =
<.014,.986>
'''

print(enumeration_ask('Raise', dict(Happy=T), happy).show_approx())
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())
'''The results mostly make sense. Since we know he is already happy, if we know that it isn't because its sunny then
there is a better chance that he got a raise, given that he is happy.'''
