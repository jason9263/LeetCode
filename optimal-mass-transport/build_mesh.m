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