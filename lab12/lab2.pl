%a.
% Exercise 2.1

% bread = bread.
%          true.

%'Bread' = bread.
%         false.

% food(X) = food(bread).
%          X = bread
%          true.

% food(bread,X) = food(Y,sausage).
%            X = sausage,
%            Y = bread.
%            true.

%meal(food(bread),X) = meal(X,drink(beer)).
%         false.
%         This does not work since X can't be both food(bread) and
%         drink(beer)

%Exercise 2.2

house_elf(dobby).
witch(hermione).
witch('McGonagall').
witch(rita_skeeter).
magic(X):- house_elf(X).
%magic(X):- wizard(X).
magic(X):- witch(X).

%?- magic(house_elf). false.
% ?- wizard(harry). ERROR: Undefined procedure: wizard/1 (DWIM could not
% correct goal) ?- magic(wizard). false. ?- magic('McGonagall'). true. ?-
% magic(Hermione). Hermione = dobby
% I needed to comment out magic(X):- wizard(X). to get it to work
%

%b.
% propositional logic does make use of unification. It allows for the
% combination of overlapping rules.
%

%c. prolog does use resolution
