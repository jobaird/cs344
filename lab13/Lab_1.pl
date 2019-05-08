%Exercise 3.2

in(X, Y) :- directlyIn(X, Y).
in(X, Z) :- directlyIn(X, Y), directlyIn(Y, Z).

directlyIn(katarina, olga).
directlyIn(olga, natasha).
directlyIn(natasha, irina).


%in(katarina, natasha).
%		true
%in(olga, katarina).
%		false

%Exercise 4.5

tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

listtrans([], []).
listtrans([G|X], [E|Y]) :- tran(G, E), listtrans(X, Y).

%b.
%Prolog does use a version of Modus Ponens. As an example, if we have bird(polly). and
%flies(X) :- bird(X). and we ask ?- flies(polly). It will return true