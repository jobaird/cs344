%Exercise 12.3

witch(X):- burns(X), looksLike(X), woman(X).
burns(X):- wood(X).
wood(X):- floats(X).
floats(X):- bread(X) ; apples(X) ; sameWeight(duck, X) ; verySmallRocks(X) ; cider(X).

bread(bread).
apples(apples).
verySmallRocks(verySmallRocks).
cider(cider).

woman(girl).
looksLike(girl).
sameWeight(duck, girl).

%?- witch(girl).
%     true

