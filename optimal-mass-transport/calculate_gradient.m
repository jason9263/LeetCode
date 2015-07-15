function D = calculate_gradient(cp,pd)
% gradient is the area of cells, parts inside the given polygon cp
nc = size(pd.cell,1);
D = zeros(nc,1);

in = true(nc,1);
in2 = inpolygon(pd.dual_point_extended(:,1),pd.dual_point_extended(:,2),cp(:,1),cp(:,2));
% find out cells not in cp completely
for i = 1:nc
    ci = pd.cell{i};
    if ~all(in2(ci))
        in(i) = false;
    end
end
cp_inverse = flipud(cp);
for i = 1:nc
    ci = pd.dual_point_extended(pd.cell{i},:);
    ci = flipud(ci);
    if in(i)
        D(i) = polyarea(ci(:,1),ci(:,2));
    else % if cell's part outside cp
        [x,y] = polybool('intersection',cp_inverse(:,1),cp_inverse(:,2),ci(:,1),ci(:,2));
        D(i) = polyarea(x,y);        
    end
end