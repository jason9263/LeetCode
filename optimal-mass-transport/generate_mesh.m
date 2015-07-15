function m = generate_mesh(type,option)
%GENERATE_MESH Genetate 2d mesh of some special type, such as square or
%circle
%   Detailed explanation goes here
if strcmp(type,'rect')
    x = reshape(repmat(linspace(option.xmin,option.xmax,option.nx)',1,option.ny),option.nx*option.ny,1);
    y = reshape(repmat(linspace(option.ymin,option.ymax,option.ny),option.nx,1),option.nx*option.ny,1);
    face = build_mesh(option.nx,option.ny);
    corner = [
        option.xmin,option.ymin;
        option.xmax,option.ymin;
        option.xmax,option.ymax;
        option.xmin,option.ymax];
    m = RectMesh(Mesh(face,[x,y]),corner);
elseif strcmp(type,'circle')
    x = [];
    y = [];
    face = [];
    m = Mesh(face,[x,y]);
end

function T = build_mesh(M,N)
% a function template
% % 
% Input
%   
% Output
%   
% % 
% Reference
% [1] 

T = zeros(2*(M-1)*(N-1),3);
X = (1:M-1)';
for j = 1:N-1
    T((j-1)*2*(M-1)+1:2:j*2*(M-1),:) = [X,X+M,X+1];
    T((j-1)*2*(M-1)+2:2:j*2*(M-1),:) = [X+1,X+M,X+M+1];
    X = X+M;
end
T(1,3) = T(2,3);
T(2,2) = T(1,1);
T(end-1,3) = T(end,3);
T(end,2) = T(end-1,1);