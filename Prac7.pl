/* reverse a list */

reverse(L):- find_reverse(L,[],L2),write("Reversed List: "),write(L2),nl.

find_reverse([],L1,L1).
find_reverse([X|TAIL],L1,L2):- find_reverse(TAIL,[X|L1],L2).

/* Position from beginning */

find_pos_beg(X,[X|_],0):-!.
find_pos_beg(X,[_|T],N):-find_pos_beg(X,T,M),N is M+1.


/* Position from end */

find_pos_end(X, L, N) :- find_reverse(L, [], L2),
                       find_pos_beg(X, L2, N).