function pd = power_diagram(point,h)

% lift point to a higher dim hyperbola
pl = [point,dot(point,point,2)-h];

face = convhull(pl);
% use face normal to filter out "upper" face, to get so-called upper
% envelop 
fn = calculate_face_normal(face,pl);
ind = fn(:,3)<0;
face = face(ind,:);

M = Mesh(face,pl);
% vfr = compute_vertex_face_ring(face);
vr = M.ComputeVertexRing();
pd.point = point;
pd.dual_point = zeros(size(face,1),2);
pd.cell = cell(size(pl,1),1);
for i = 1:size(face,1)
    dp = face_dual_point(pl(face(i,:),:));
    pd.dual_point(i,:) = dp;
end
K = convhull(point);
vb = zeros(size(K,1)-1,2);
mindp = min(pd.dual_point)-1;
maxdp = max(pd.dual_point)+1;
minx = mindp(1);
miny = mindp(2);
maxx = maxdp(1);
maxy = maxdp(2);
box = [minx,miny;maxx,miny;maxx,maxy;minx,maxy;minx,miny];
% box = [min(pd.dp)-1,max(pd.dp)+1];
for i = 1:size(K,1)-1
    i1 = K(i);
    i2 = K(i+1);
    vec = point(i1,:)-point(i2,:);
    ip = polygon_line_intersection(box,[vec,dot(point(i2,:),point(i2,:))/2-dot(point(i1,:),point(i1,:))/2]);
    if det([1,point(i1,:);1,point(i2,:);1,ip(1,:)])<0
        vb(i,:) = ip(1,:);
    else
        vb(i,:) = ip(2,:);
    end
end
pd.dual_point_extended = [pd.dual_point;vb];
for i = 1:size(point,1)
    vri = vr{i};
    pb = find(K==i,1,'first');
    if pb
        fr = zeros(1,length(vri)+1);
        fr(end) = size(face,1)+pb;
        if pb == 1
            fr(1) = size(face,1)+size(K,1)-1;
        else
            fr(1) = size(face,1)+pb-1;
        end
        for j = 1:length(vri)-1
            fr(j+1) = M.VViF(i,vri(j));
        end
    else
        fr = zeros(size(vri));
        for j = 1:length(vri)
            fr(j) = M.VViF(i,vri(j));
        end
    end
    pd.cell{i} = fr(end:-1:1);
end


function dp = face_dual_point(p)
% dual point of a triangle face
a=p(1,2)*(p(2,3)-p(3,3))+p(2,2)*(p(3,3)-p(1,3))+p(3,2)*(p(1,3)-p(2,3));
b=p(1,3)*(p(2,1)-p(3,1))+p(2,3)*(p(3,1)-p(1,1))+p(3,3)*(p(1,1)-p(2,1));
c=p(1,1)*(p(2,2)-p(3,2))+p(2,1)*(p(3,2)-p(1,2))+p(3,1)*(p(1,2)-p(2,2));
% d=-1*(p(1,1)*(p(2,2)*p(3,3)-p(3,2)*p(2,3))+p(2,1)*(p(3,2)*p(1,3)-p(1,2)*p(3,3))+p(3,1)*(p(1,2)*p(2,3)-p(2,2)*p(1,3)));	
dp = [-a/c/2, -b/c/2];