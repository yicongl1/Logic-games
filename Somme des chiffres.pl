chiffre(X) :-
    member(X, [1,2,3,4,5,6,7,8,9,0]).

generate(X1, X2) :-
    chiffre(X1),
    chiffre(X2),
    X1 =< X2.

test(X1, X2, X) :-
    generate(X1, X2),
    X1 + X2 =:= X.
    
solve(X1, X2, X) :-
    generate(X1, X2),
    test(X1, X2, X).
    