nBienPlace([], [], 0).
nBienPlace([X|Ci], [X|Cp], BP) :- 
    nBienPlace(Ci, Cp, BPTmp), 
    BP is BPTmp + 1.
nBienPlace([A|Ci], [B|Cp], BP) :- 
    dif(A, B), 
    nBienPlace(Ci, Cp, BP).

gagne([], []).
gagne([X|Ci], [X|Cp]) :- gagne(Ci, Cp).

element(E, [H|R]) :- dif(E, H), element(E, R).
element(E, [E|_]).

enleve(_, [], []).
enleve(E, [E|L1], L2) :- enleve(E, L1, L2).
enleve(E, [H|L1], [H|L2Tmp]) :- 
    dif(E, H), 
    enleve(E, L1, L2Tmp).

enleveBP([], [], [], []).
enleveBP([H|C1Tmp], [H|C2Tmp], C1B, C2B) :- 
    enleveBP(C1Tmp, C2Tmp, C1B, C2B).
enleveBP([H1|C1Tmp], [H2|C2Tmp], [H1|C1BTmp], [H2|C2BTmp]) :-
    dif(H1,H2),
    enleveBP(C1Tmp, C2Tmp, C1BTmp, C2BTmp).
 
nMalPlacesAux([], _, 0).
nMalPlacesAux([H|C1], C2, MP) :-
    element(H, C2),
    nMalPlacesAux(C1, C2, MPTmp),
    MP is MPTmp + 1.
nMalPlacesAux([H|C1], C2, MP) :-
    \+ element(H, C2),
    nMalPlacesAux(C1, C2, MP).

nMalPlaces(C1, C2, MP) :-
    enleveBP(C1, C2, C1B, C2B),
    nMalPlacesAux(C1B, C2B, MP).

codeur(_, 0, []).
codeur(M, N, Code) :-
    NTmp is N - 1,
    MTmp is M + 1,
    random(1, MTmp, Num),
    codeur(M, NTmp, CodeTmp),
    Code = [Num|CodeTmp].

jouons(M, N, Max) :-
    codeur(M, N, C1),
    jouonsC(C1, Max).
jouonsC(C1, 0) :-
    write("Perdu !!!"),
    nl,
    write("Code initial: "),
    write(C1).
jouonsC(C1, Max) :- 
    Max > 0,
    write("Il reste "), 
    write(Max), 
    write(" coup(s)."),
    nl,
    write("Donner un code : "),
    read(C2),
    nBienPlace(C1, C2, BP),
    nMalPlaces(C1, C2, MP),
    write("BP: "),
    write(BP),
    write("/MP: "),
    write(MP),
    nl,
    (gagne(C1,C2) -> 
    	write("Gagné !!!")
    ;   
    	MaxTmp is Max - 1,
    	jouonsC(C1, MaxTmp)
    ).


    
    


