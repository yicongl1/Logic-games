% debut bloc
pere(X,Y) :- parent(X,Y), homme(X).
mere(X,Y) :- parent(X,Y), femme(X).
epoux(X,Y) :- couple(X,Y), homme(X).
epoux(X,Y) :- couple(Y,X), homme(X).
epouse(X,Y) :- couple(X,Y), femme(X).
epouse(X,Y) :- couple(Y,X), femme(X).
fils(X,Y) :- parent(Y,X), homme(X).
fille(X,Y) :- parent(Y,X), femme(X).
enfant(X,Y) :- parent(Y,X).
grandPere(X,Y) :- pere(X,Z), parent(Z,Y).
grandMere(X,Y) :- mere(X,Z), parent(Z,Y).
grandParent(X,Y) :- parent(X,Z), parent(Z,Y).
petitFils(X,Y) :- grandParent(Y,X), homme(X).
petiteFille(X,Y) :- grandParent(Y,X), femme(X).
memePere(X,Y) :- pere(Z,X), pere(Z,Y), X\=Y.
memeMere(X,Y) :- mere(Z,X), mere(Z,Y), X\=Y.
memeParent(X,Y) :- parent(Z,X), parent(Z,Y), X\=Y.
memeParents(X,Y) :- memePere(X,Y), memeMere(X,Y).
frere(X,Y) :- memeParents(X,Y), homme(X).
soeur(X,Y) :- memeParents(X,Y), femme(X).
demiFrere(X,Y) :- memeParent(X,Y), \+(memeParents(X,Y)), homme(X).
demiSoeur(X,Y) :- memeParent(X,Y), \+(memeParents(X,Y)), femme(X).
oncle(X,Y) :- parent(Z,Y), frere(X,Z).
oncle(X,Y) :- epoux(X,Z), soeur(Z,W), parent(W,Y).
tante(X,Y) :- parent(Z,Y), soeur(X,Z).
tante(X,Y) :- epouse(X,Z), frere(Z,W), parent(W,Y).
neveu(X,Y) :- oncle(Y,X), homme(X).
neveu(X,Y) :- tante(Y,X), homme(X).
niece(X,Y) :- oncle(Y,X), femme(X).
niece(X,Y) :- tante(Y,X), femme(X).
cousin(X,Y) :- fils(X,Z), oncle(Z,Y).
cousin(X,Y) :- fils(X,Z), tante(Z,Y).
cousine(X,Y) :- fille(X,Z), oncle(Z,Y).
cousine(X,Y) :- fille(X,Z), tante(Z,Y).
gendre(X,Y) :- epoux(X,Z), enfant(Z,Y).
bru(X,Y) :- epouse(X,Z), enfant(Z, Y).
maratre(X,Y) :- epouse(X,Z), pere(Z,Y), \+(mere(X,Y)).
belleMere(X,Y) :- mere(X,Z), couple(Y,Z).
belleMere(X,Y) :- mere(X,Z), couple(Z,Y).
beauPere(X,Y) :- pere(X,Z), couple(Y,Z).
beauPere(X,Y) :- pere(X,Z), couple(Z,Y).
ascendant(X,Y) :- parent(X,Y).
ascendant(X,Y) :- ascendant(Z,Y), parent(X,Z).
descendant(X,Y) :- ascendant(Y,X).
lignee(X,Y) :- descendant(X,Y).
lignee(X,Y) :- descendant(Y,X).
parente(X,Y) :- ascendant(Z,X), ascendant(Z,Y).
% fin bloc
