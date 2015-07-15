% create some random point in unit circle
v = rand(10,2)*2-1;
in = dot(v,v,2)<1;
point = v(in,:);
% create unit circle
t = 0:2*pi/36:2*pi;
disk = [cos(t);sin(t)]';
% set area to be equal in all cells
area = polyarea(disk(:,1),disk(:,2))*ones(size(point,1),1)/size(point,1);
% initial power diagram
pd0 = power_diagram(point,zeros(size(point,1),1));

% compute power diagram with desired area
[pd,h] = discrete_optimal_transport(disk,point,area);

%% plot result
figure
plot_power_diagram(pd0);
title('initial power diagram')
hold on
plot(disk(:,1),disk(:,2),'r-')
axis([-1 1 -1 1])
figure;
plot_power_diagram(pd);
title('final power diagram')
hold on
plot(disk(:,1),disk(:,2),'r-')
axis([-1 1 -1 1])