% set x and y as a symbol
syms u v

% function of x,y
f1 = (-1/3)*(u/(v+1))^4;
pretty(f1)

% compute mass, with is the integral of density
% depend on the nature of the area
% This case we have to use double derivative
F1 = int(f1, u, 2, 4);
F2 = int(F1,v,0,4);
pretty(F2)
% compute moment respect to y
f = y*(5 + y);
F = int(f, y, 0, sqrt(1-(x^2/36)))
final = int(F,x,-6,6)

%display result
pretty(final/final1)