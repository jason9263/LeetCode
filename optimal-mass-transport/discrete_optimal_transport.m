function [pd,h] = discrete_optimal_transport(cp,point,area)
% Discrete Optimal Transport
% cp: convex polytope
% point: k distinc point in R^n
% area: k positive scaler s.t. sum(area) = vol(cp)

np = size(point,1);
h = zeros(np,1);
pd = power_diagram(point,h);
k = 1;
tic;
while true
    D = calculate_gradient(cp,pd)-area;
    H = calculate_hessian(cp,pd);
    H(1,1) = H(1,1)+1;
    dh = H\D;
    dh = dh - mean(dh);
    h = h - dh;
    str = sprintf('#%02d: max|dh| = %.10f',k,max(abs(dh)));
    disp(str);
    if max(abs(dh)) < 1e-6
        break
    end
    
%     cla
%     plot_power_diagram(pd);
%     hold on
%     plot(cp(:,1),cp(:,2),'r-');
%     pause(0.1)
    
    pd = power_diagram(point,h);
    k = k+1;
end
toc;