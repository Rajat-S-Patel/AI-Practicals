insert_beg(X,L,[X|L]). 
insert_beg(X,L):-insert_beg(X,L,Z),write("Updated List is:"),write(Z). 

insert_tail(X,[],[X]). 
insert_tail(X,[Y|T],[Y|T1]):-insert_tail(X,T,T1). 
insert_tail(X,L):-insert_tail(X,L,Z),write("Updated List is:"),write(Z). 

insert_pos(X,L,0,[X|L]). 
insert_pos(X,[Y|T],Pos,N) :- Pos2 is Pos-1,insert_pos(X,T,Pos2,Temp),insert_beg(Y,Temp,N).