member(X,[],N):-write("\nMember not found"). 
member(X,[X|T],N):-write("\nMember found at index"),write(N). 
member(X,[_|T],N):-N1 is N+1,member(X,T,N1). 
member(X,Y):-member(X,Y,0). 
test(X):-write(X).