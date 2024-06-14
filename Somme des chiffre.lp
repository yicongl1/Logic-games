#const n = 25.
nombre(1..n).
norme(X, Y) :- 
  nombre(X),
  nombre(Y),
  X**2 + Y**2 = n.
  
#show norme/2.