#const n = 25.
nombre(1..n).
norme(X, Y) :- 
  nombre(X),
  nombre(Y),
  X**2 + Y**2 = n.

{norme(X, Y): nombre(X), nombre(Y)} = 1.
:- norme(X, Y), not X**2 + Y**2 = n.
:- norme(X, Y), X<Y.
#show norme/2.

#show norme/2.