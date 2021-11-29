rev(L) :- findrev(L, [], L2), write(L2), nl.

findrev([], L1, L1).

findrev([X|Tail], L1, L2) :- findrev(Tail, [X|L1], L2).

findbeg(X,[X|_],1):-!.
findbeg(X,[_|Tail],N):-findbeg(X,Tail,NN),N is NN+1.

findend(X, List, N) :- findrev(List, [], List2),
                       findbeg(X, List2, N).