function H = calculate_hessian(cp,pd)
nc = size(pd.cell,1);
ne = (sum(cellfun(@length,pd.cell))-nc);
I = zeros(ne,1);
J = zeros(ne,1);
V = zeros(ne,1);
k = 1;
for i = 1:nc
    ci = pd.cell{i};
    for j = 1:length(ci)-1
        I(k) = ci(j);
        J(k) = ci(j+1);
        V(k) = i;
        k = k+1;
    end
end
C = sparse(I,J,V);
[I,J,~] = find(C);
I2 = zeros(ne,1);
J2 = zeros(ne,1);
V2 = zeros(ne,1);
k = 1;
in = inpolygon(pd.dual_point_extended(:,1),pd.dual_point_extended(:,2),cp(:,1),cp(:,2));
for i = 1:length(I)
        I2(k) = C(I(i),J(i));
        J2(k) = C(J(i),I(i));
        % compute edge length in convex polygon
        p1 = pd.dual_point_extended(I(i),:);
        p2 = pd.dual_point_extended(J(i),:);
        in2 = in([I(i) J(i)]);
        switch sum(in2)
            case 2 % if both points in polygon
                lij = norm(p1-p2);
            case 1 % if one point inside, one outside
                pi = polygon_line_intersection(cp,[p1;p2]);
                if in2(1)
                    lij = norm(pi-p1);
                else
                    lij = norm(pi-p2);
                end
            case 0 % both point outside the polygon
                lij = 0;
        end
        V2(k) = -lij/norm(pd.point(I2(k),:)-pd.point(J2(k),:));
        k = k+1;
end
H = sparse(I2,J2,V2);
Hs = -sum(H,2);
H = H + sparse(diag(Hs));