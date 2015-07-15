function v = omt(face,uv,mu1,mu2)
%OMT 
%   
t = linspace(0,1,20);

for i = 1:length(t)
    m1 = mu1(face,uv);
    m2 = mu2(face,uv);
    rho = (1-t(i))*m1+t(i)*m2;
    A = generalized_laplace(face,uv,rho);
    b = m2 - m1;
    phi = A\b;
    phi = phi - mean(phi);
    v = grad(face,uv,phi);
end

end

function A = generalized_laplace(face,uv,rho)
fa = face_area(face,uv);
f0 = face(:,1);
f1 = face(:,2);
f2 = face(:,3);

uxv0 = uv(f1,2) - uv(f2,2);
uyv0 = uv(f2,1) - uv(f1,1);
uxv1 = uv(f2,2) - uv(f0,2);
uyv1 = uv(f0,1) - uv(f2,1);
uxv2 = uv(f0,2) - uv(f1,2);
uyv2 = uv(f1,1) - uv(f0,1);

% uxv0 = rho(f1).*uv(f1,2) - rho(f2).*uv(f2,2);
% uyv0 = rho(f2).*uv(f2,1) - rho(f1).*uv(f1,1);
% uxv1 = rho(f2).*uv(f2,2) - rho(f0).*uv(f0,2);
% uyv1 = rho(f0).*uv(f0,1) - rho(f2).*uv(f2,1);
% uxv2 = rho(f0).*uv(f0,2) - rho(f1).*uv(f1,2);
% uyv2 = rho(f1).*uv(f1,1) - rho(f0).*uv(f0,1);

v00 = (rho(f0).*uxv0.*uxv0 + rho(f0).*uyv0.*uyv0)./fa/4;
v11 = (rho(f1).*uxv1.*uxv1 + rho(f1).*uyv1.*uyv1)./fa/4;
v22 = (rho(f2).*uxv2.*uxv2 + rho(f2).*uyv2.*uyv2)./fa/4;

v01 = (rho(f0).*uxv1.*uxv0 + rho(f1).*uyv1.*uyv0)./fa/4;
v10 = (rho(f1).*uxv1.*uxv0 + rho(f0).*uyv1.*uyv0)./fa/4;
v12 = (rho(f1).*uxv2.*uxv1 + rho(f2).*uyv2.*uyv1)./fa/4;
v21 = (rho(f2).*uxv2.*uxv1 + rho(f1).*uyv2.*uyv1)./fa/4;
v20 = (rho(f2).*uxv0.*uxv2 + rho(f0).*uyv0.*uyv2)./fa/4;
v02 = (rho(f0).*uxv0.*uxv2 + rho(f2).*uyv0.*uyv2)./fa/4;

I = [f0;f1;f2;f0;f1;f1;f2;f2;f0];
J = [f0;f1;f2;f1;f0;f2;f1;f0;f2];
V = [v00;v11;v22;v01;v10;v12;v21;v20;v02];
A = sparse(I,J,-V);
end