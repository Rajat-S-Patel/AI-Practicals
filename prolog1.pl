/* FACTS */

parent(sanjay,rajat).
parent(varsha,rajat).
parent(shivaram,sanjay).
parent(kamla,sanjay).
parent(sita,varsha).
parent(kanti,varsha).
parent(sanjay,shreya).
parent(varsha,shreya).
parent(shivaram,sonal).
parent(kamla,sonal).

female(shreya).
female(varsha).
female(kamla).
female(sita).
female(sonal).
male(rajat).
male(sanjay).
male(shivaram).
male(kanti).



mother(X,Y):-parent(X,Y),female(X).
sister(X,Y):-parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.
grandfather(X,Y):-parent(Z,Y),parent(X,Z),male(X).
grandmother(X,Y):-parent(Z,Y),parent(X,Z),female(X).
aunt(X,Y):-parent(Z,Y),brother(Z,X),female(X).
father(X,Y):-parent(X,Y),male(X).