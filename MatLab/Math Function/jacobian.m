% x = v + w, y = u + w, z= 3u+3v
syms u v w;
det(jacobian([v+w,u+w,3*u+3*v],[u,v,w]))