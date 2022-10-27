function final = jacobian_trans(f1,f2)

    syms u v
    final = diff(f1,u)*diff(f2,v) - diff(f1,v)*diff(f2,u)
end
