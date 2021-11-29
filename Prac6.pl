list_member(X,[X|_]).
list_member(X,[_|TAIL]) :- list_member(X,TAIL).

list_insert_begin(X,LIST,[X|LIST]).

list_insert_end(X,[],[X]).
list_insert_end(X,[H|T],[H|T2]):- list_insert_end(X,T,T2).

list_insert_pos(X,0,L,[X|L]).
list_insert_pos(X,Pos,[E|L],ZL):- 
    Pos1 is Pos-1, list_insert_pos(X,Pos1,L,ZL1),
    list_insert_begin(E,ZL1,ZL).