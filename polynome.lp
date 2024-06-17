%https://potassco.org/clingo/run/
#const n=10.
intervalle(-n..n).
p1(X, Y) :- 
  intervalle(X), 
  Y = X**2 + 2*X - 3.
p2(X, Y) :-
  intervalle(X),
  Y = X**2 - 1.
p3(X, Y) :-
  intervalle(X),
  Y = X**2 + 1.
{p(X, Y): p3(X, Y)} = 1.
:- p(X, Y), Y != 0.
#show p/2.