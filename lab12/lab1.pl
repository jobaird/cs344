% Exercise 1:

% a.:
% Exercise 1.4

killer(butch).

married(mia, marsellus).

dead(zed).

kills(marsellus, X):- givesFootMassage(X, mia).

loves(mia, X):- goodDancer(X).

eats(jules, X):- nutritious(X) ; tasty(X).

% Exercise 1.5

wizard(ron).
hasWand(harry).
quidditchPlayer(harry).
wizard(X):- hasBroom(X), hasWand(X).
hasBroom(X):- quidditchPlayer(X).

% wizard(ron).
% yes

% witch(ron).
% undefined procedure

%wizard(hermione).
% no

% wizard(harry).
% yes

%wizard(Y).
% Y = harry ;
% Y = ron

%witch(Y).
% undefined procedure

%prolog is able to display who is a wizard, and reason backwards from the fact harry has a wand
% so he must be a wizard, it cannot recognize witch, since it has no info on witch.

%b. yes, it can be implemented in prolog.

q :- p.
p.

% q.
% RETURN: true.

%Horn clauses make use of variables, but can only imply one thing, while propositional logic can imply
%conjunctions and disjunctions.

%d. prolog does support this distinction. As you tell the program what the rules are and query based off what you told it

