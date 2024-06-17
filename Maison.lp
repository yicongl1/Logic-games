nationalite(esp, ita, nor).
couleur(bleu, vert, rouge).
{maison(N, Cou, Nat): couleur(Cou), nationalite(Nat)} = 1 :- N =1..3.
:- maison(I, C, _), maison(I, C, _), I!=J